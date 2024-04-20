# -*- coding: utf-8 -*-

import os

if not os.path.exists('docs'):
    os.makedirs('docs')
import pdfplumber
import numpy as np
import torch
from transformers import BertForQuestionAnswering, BertTokenizer
from flask import Flask, request, render_template, redirect, url_for
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Initialize Firebase
cred = credentials.Certificate('C:/Users/MohdS/OneDrive/Desktop/Major-Project/credentials.json')
firebase_admin.initialize_app(cred, {
    'projectId': 'testing-58ac9',
})

app = Flask(__name__)

def pdf_extract(file_name):
    pdf_txt = ""
    try:
        with pdfplumber.open(os.path.join("docs", file_name)) as pdf:
            for pdf_page in pdf.pages:
                single_page_text = pdf_page.extract_text()
                pdf_txt += single_page_text
        store_pdf_text(file_name, pdf_txt)
    except FileNotFoundError:
        # Handle case where the file is not found
        return "File not found: {}".format(file_name)
    return pdf_txt


def store_pdf_text(file_name, pdf_text):
    db = firestore.client()
    doc_ref = db.collection('pdf_data').document(file_name)
    doc_ref.set({'text': pdf_text})

def get_pdf_text(file_name):
    db = firestore.client()
    doc_ref = db.collection('pdf_data').document(file_name)
    doc = doc_ref.get()
    if doc.exists:
        return doc.to_dict()['text']
    else:
        return None

def bert_drive(file_name, question):
    text = pdf_extract(file_name)
    if text:
        max_score = 0
        final_answer = ""
        new_df = expand_split_sentences(text)
        tokens = []
        s_scores = np.array([])
        e_scores = np.array([])

        for new_context in new_df:
            ans, score, start_score, end_score, token = bert_qa(question, new_context)
            if score > max_score:
                max_score = score
                start_score_tensor = torch.tensor(start_score)
                end_score_tensor = torch.tensor(end_score)
                s_scores = start_score_tensor.detach().numpy()
                e_scores = end_score_tensor.detach().numpy()
                tokens = token
                final_answer = ans

        return final_answer, s_scores, e_scores, tokens
    else:
        return "Sorry, couldn't retrieve the PDF text from Firebase.", [], [], []

def expand_split_sentences(pdf_txt):
    import nltk
    nltk.download('punkt', quiet=True)
    new_chunks = nltk.sent_tokenize(pdf_txt)
    new_df = []
    for i in range(len(new_chunks)):
        paragraph = ""
        for j in range(i, len(new_chunks)):
            tmp_token = tokenizer.encode(paragraph + new_chunks[j])
            if len(tmp_token) < 510:
                paragraph += new_chunks[j]
            else:
                break
        new_df.append(paragraph)
    return new_df

# BERT-related setup
model = BertForQuestionAnswering.from_pretrained('bert-large-uncased-whole-word-masking-finetuned-squad')
tokenizer = BertTokenizer.from_pretrained('bert-large-uncased-whole-word-masking-finetuned-squad')

def bert_qa(question, context, max_len=500):

    #Tokenize input question and passage 
    #Add special tokens - [CLS] and [SEP]
    input_ids = tokenizer.encode (question, context,  max_length= max_len, truncation=True)  


    #Getting number of tokens in question and context passage that contains the answer
    sep_index = input_ids.index(102) 
    len_question = sep_index + 1   
    len_context = len(input_ids)- len_question  

    
    #Separate question and context 
    #Segment ids will be 0 for question and 1 for context
    segment_ids =  [0]*len_question + [1]*(len_context)  

    #Converting token ids to tokens
    tokens = tokenizer.convert_ids_to_tokens(input_ids) 


    #Getting start and end scores for answer
    #Converting input arrays to torch tensors before passing to the model
    start_token_scores = model(torch.tensor([input_ids]), token_type_ids=torch.tensor([segment_ids]) )[0]
    end_token_scores = model(torch.tensor([input_ids]), token_type_ids=torch.tensor([segment_ids]) )[1]


    #Converting scores tensors to numpy arrays
    start_token_scores = start_token_scores.detach().numpy().flatten()
    end_token_scores = end_token_scores.detach().numpy().flatten()

    #Getting start and end index of answer based on highest scores
    answer_start_index = np.argmax(start_token_scores)
    answer_end_index = np.argmax(end_token_scores)


    #Getting scores for start and end token of the answer
    start_token_score = np.round(start_token_scores[answer_start_index], 2)
    end_token_score = np.round(end_token_scores[answer_end_index], 2)


    #Combining subwords starting with ## and get full words in output. 
    #It is because tokenizer breaks words which are not in its vocab.
    answer = tokens[answer_start_index] 
    for i in range(answer_start_index + 1, answer_end_index + 1):
        if tokens[i][0:2] == '##':  
            answer += tokens[i][2:] 
        else:
            answer += ' ' + tokens[i]  

    # If the answer not in the passage
    if ( answer_start_index == 0) or (start_token_score < 0 ) or  (answer == '[SEP]') or ( answer_end_index <  answer_start_index):
        answer = "Sorry, Couldn't find answer in given pdf. Please try again!"
    
    return (answer_start_index, answer_end_index, start_token_score, end_token_score,  answer)

    pass

app = Flask(__name__, template_folder='templates')

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
            if file_name is None:
                return "No file selected!"
            answer, s_scores, e_scores, tokens = bert_drive(file_name, question)
            return render_template('qa.html', answer=answer, question=question)
    return render_template('index.html')


@app.route('/upload/', methods=['GET', 'POST'])
def upload():
    return render_template('upload.html')

@app.route('/qa/', methods=['GET', 'POST'])
def qa():
    file_names = [f for f in os.listdir("docs")]
    return render_template('qa.html', file_names=file_names)

if __name__ == '__main__':
    app.run(debug=True)