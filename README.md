# Major Project: Document Question Answering System

This repository contains code, documents, references, and resources for the Major Project (Batch 2024).

## Overview

The Document Question Answering System is a Flask web application that enables users to upload PDF files and ask questions related to their content. It leverages NLP techniques, particularly the fine-tuned Bidirectional Encoder Representations from Transformers (BERT) model, for accurate question answering.

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

For a deeper understanding of BERT architecture, you can refer to [this explanatory resource](link/to/resource).

## System Design

The project adheres to a well-defined system design documented in the Major Project PPT file, including:

- **Use Case Diagram:** Illustrates interactions between users and the system (e.g., uploading PDFs, asking questions, viewing answers).
  
- **Sequence Diagrams:** Describes interactions between system components (e.g., file upload handling, question processing, response rendering).
  
- **Flowchart:** Provides a visual representation of program execution, including operations and decision points.
  
- **ER Diagram (if applicable):** Depicts data entities and their relationships within the system.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/document-qa-system.git
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

This project is licensed under the MIT License.