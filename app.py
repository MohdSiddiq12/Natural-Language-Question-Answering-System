# -*- coding: utf-8 -*-
import os
import pdfplumber
import torch
import numpy as np
from transformers import BertForQuestionAnswering, BertTokenizer
from flask import Flask, request, render_template, redirect, url_for
from werkzeug.utils import secure_filename
import joblib
from concurrent.futures import ThreadPoolExecutor, as_completed
import nltk

app = Flask(__name__)

# BERT-related setup
model = joblib.load('bert_model.pkl')
tokenizer = joblib.load('bert_tokenizer.pkl')

def pdf_extract(file_name):
    pdf_txt = ""
    file_path = os.path.join("docs", file_name)
    if not os.path.exists(file_path):
        return None
    try:
        with pdfplumber.open(file_path) as pdf:
            for pdf_page in pdf.pages:
                single_page_text = pdf_page.extract_text()
                if single_page_text:
                    pdf_txt += single_page_text
    except Exception as e:
        print(f"Error extracting text from PDF: {e}")
        return None
    return pdf_txt

def expand_split_sentences(pdf_txt):
    nltk.download('punkt', quiet=True)
    sentences = nltk.sent_tokenize(pdf_txt)
    chunks = []
    current_chunk = []
    chunk_size = 500  # Adjust chunk size based on BERT's token limit (512 tokens)

    for sentence in sentences:
        current_chunk.append(sentence)
        if len(tokenizer.encode(" ".join(current_chunk))) > chunk_size:
            current_chunk.pop()
            chunks.append(" ".join(current_chunk))
            current_chunk = [sentence]
    
    if current_chunk:
        chunks.append(" ".join(current_chunk))
    
    return chunks

def get_answer(question, context):
    try:
        inputs = tokenizer.encode_plus(question, context, return_tensors='pt')
        input_ids = inputs['input_ids'].tolist()[0]

        text_tokens = tokenizer.convert_ids_to_tokens(input_ids)
        sep_index = input_ids.index(tokenizer.sep_token_id)
        len_question = sep_index + 1
        len_context = len(input_ids) - len_question

        segment_ids = [0] * len_question + [1] * len_context

        outputs = model(**inputs)
        start_scores = outputs.start_logits
        end_scores = outputs.end_logits

        start_scores = start_scores.detach().numpy().flatten()
        end_scores = end_scores.detach().numpy().flatten()

        answer_start_index = np.argmax(start_scores)
        answer_end_index = np.argmax(end_scores)

        start_token_score = np.round(start_scores[answer_start_index], 2)
        end_token_score = np.round(end_scores[answer_end_index], 2)

        answer = text_tokens[answer_start_index]
        for i in range(answer_start_index + 1, answer_end_index + 1):
            if text_tokens[i][0:2] == '##':
                answer += text_tokens[i][2:]
            else:
                answer += ' ' + text_tokens[i]

        if (answer_start_index == 0) or (start_token_score < 0) or (answer == '[SEP]') or (answer_end_index < answer_start_index):
            return (start_token_score, end_token_score, "Sorry, Couldn't find answer in the given PDF. Please try again!", context)
        
        additional_context = " ".join(text_tokens[max(0, answer_start_index-20):min(len(text_tokens), answer_end_index+20)])
        return (start_token_score, end_token_score, answer, additional_context)
    except Exception as e:
        print(f"Error getting answer: {e}")
        return (0, 0, "Sorry, Couldn't find answer in the given PDF. Please try again!", context)

def bert_drive(file_name, question):
    text = pdf_extract(file_name)
    if not text:
        return "Sorry, couldn't retrieve the PDF text."
    
    chunks = expand_split_sentences(text)
    max_workers = min(10, len(chunks))
    results = []

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_chunk = {executor.submit(get_answer, question, chunk): chunk for chunk in chunks}
        for future in as_completed(future_to_chunk):
            try:
                result = future.result()
                results.append(result)
            except Exception as e:
                print(f"Error processing chunk: {e}")

    if not results:
        return "Sorry, Couldn't find answer in the given PDF. Please try again!"

    best_result = max(results, key=lambda x: x[0] if x else 0)
    best_answer, additional_context = best_result[2], best_result[3]
    full_answer = f"Answer: {best_answer}\n\nAdditional Context: {additional_context}"
    return full_answer

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form.get('btn') == 'index':
            if 'upload' not in request.files:
                return "No file selected!"
            upload = request.files['upload']
            if upload.filename == '':
                return "No file selected!"
            file_name = secure_filename(upload.filename)
            upload.save(os.path.join("docs", file_name))
            return redirect(url_for('qa', file_name=file_name))
        elif request.form.get('btn') == 'qa':
            question = request.form.get('question')
            file_name = request.form.get('file_name')
            if not file_name:
                return "No file selected!"
            answer = bert_drive(file_name, question)
            return render_template('qa.html', answer=answer, question=question, file_name=file_name)
    return render_template('index.html')

@app.route('/upload/', methods=['GET', 'POST'])
def upload():
    return render_template('upload.html')

@app.route('/qa/', methods=['GET', 'POST'])
def qa():
    file_name = request.args.get('file_name')
    if not file_name:
        return "No file selected"
    file_names = [f for f in os.listdir("docs") if os.path.isfile(os.path.join("docs", f))]
    return render_template('qa.html', file_names=file_names, file_name=file_name)

if __name__ == '__main__':
    app.run(debug=False)