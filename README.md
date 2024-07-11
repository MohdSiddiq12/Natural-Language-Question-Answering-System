# Natural Laguage Question Answering System

This repository contains code, documents, references, and resources for the Major Project (Batch 2024).

## Overview

Natural Laguage Question Answering System is a Flask web application that enables users to upload PDF files and ask questions related to their content. It leverages NLP techniques, particularly the fine-tuned Bidirectional Encoder Representations from Transformers (BERT) model, for accurate question answering.

## Features

- Upload PDF files
- Ask questions related to uploaded PDF content
- Obtain answers extracted from the PDF using BERT
- Handle long documents with intelligent splitting and context preservation
- Display answers with relevant context from the PDF
- Easy-to-use web interface

## Architecture

This client-server system comprises a Flask backend and a web frontend. Key components include:

- **BERT Model:** The fine-tuned BERT model converts questions and document content into semantic representations for accurate answer identification.
- **Document Processing:** The system employs the `expand_split_sentences` function to handle long documents exceeding BERT's token limit. It intelligently splits paragraphs while preserving context.
- **Answer Extraction:** Combining extractive and abstractive summarization techniques, the system provides concise and informative answers from relevant passages.
- **Web Interface:** The Flask backend serves a user-friendly interface for uploading PDFs, entering questions, and viewing extracted answers with context.

### BERT Architecture (Optional)

For a deeper understanding of BERT architecture, you can refer to [this explanatory resource](https://en.wikipedia.org/wiki/BERT_(language_model)).

## System Design

The project adheres to a well-defined system design documented in the Major Project PPT file, including:

- **Use Case Diagram:** Illustrates interactions between users and the system (e.g., uploading PDFs, asking questions, viewing answers).
- **Sequence Diagrams:** Describes interactions between system components (e.g., file upload handling, question processing, response rendering).
- **Flowchart:** Provides a visual representation of program execution, including operations and decision points.
- **ER Diagram (if applicable):** Depicts data entities and their relationships within the system.

## Results

Here are some screenshots showcasing the Document Question Answering System:

### Home Screen
![Home-Screen](https://github.com/MohdSiddiq12/Python-exercise/assets/97431769/70ca03c9-a1cb-404c-ba7b-482c326805f6)

### Upload PDF File

![Upload](https://github.com/MohdSiddiq12/Python-exercise/assets/97431769/70dd0c06-ec45-4775-a5dc-b775dff072c9)


### File Selected

![File_Selected](https://github.com/MohdSiddiq12/Python-exercise/assets/97431769/d5498473-ee1c-441f-90db-1700d9a571db)

### Question Answering


![Question_Answering](https://github.com/MohdSiddiq12/Python-exercise/assets/97431769/edf62b37-3265-4e0b-bcf1-593ff4720f98)





## Installation

1. Clone the repository:

```bash
git clone https://github.com/MohdSiddiq12/Major-Project
```

**Note:** Use code with caution.

2. Install dependencies:

```bash
pip install -r requirements.txt
```

**Note:** Use code with caution.

3. Download the pre-trained BERT model and tokenizer (replace with download instructions). Save them as `bert_model.pkl` and `bert_tokenizer.pkl` in the project directory.

4. Run the Flask application:

```bash
python app.py
```

**Note:** Use code with caution.

5. Access the web interface: [http://localhost:5000](http://localhost:5000) in your browser.

## Contributing

Contributions are welcome! If you encounter issues or have suggestions, please open an issue or submit a pull request.

## License

This project is licensed under the Apache License.
