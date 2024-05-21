Major-Project

Code, Documents, References & Resources for Major Project (Batch 2024)

Document Question Answering System using NLP Techniques
This Flask web application allows users to upload PDF files and ask questions related to their content. It utilizes the fine-tuned Bidirectional Encoder Representations from Transformers (BERT) model for question answering, combining NLP techniques with deep learning for accurate answers.

Features

Upload PDF files
Ask questions related to the uploaded PDF content
Get answers extracted from the PDF using BERT
Handle long documents with intelligent splitting and context preservation
Display answers with relevant context from the PDF
Easy-to-use web interface
Architecture

This client-server system uses a Flask backend and a web frontend. Core components include:

BERT Model: The fine-tuned BERT model converts questions and document content into semantic representations, enabling accurate answer identification.

Document Processing: The expand_split_sentences function handles long documents exceeding BERT's token limit. It intelligently splits paragraphs while preserving context.

Answer Extraction: The system combines extractive and abstractive summarization techniques to provide concise and informative answers from relevant passages.

Web Interface: The Flask backend serves a user-friendly interface for uploading PDFs, entering questions, and viewing extracted answers with context.

BERT Architecture (Optional)

Consider including a link to an explanatory resource on BERT architecture (like the one provided for BERT itself) if you want to delve deeper.

System Design

The project follows a well-defined system design documented in the Major Project PPT file (UML diagrams, sequence diagrams). Key components include:

Use Case Diagram: Interactions between users and the system (upload PDFs, ask questions, view answers).
Sequence Diagrams: Interactions between system components (file upload handling, question processing, response rendering).
Flowchart: Visual representation of program execution (operations and decision points).
ER Diagram (if applicable): Data entities and their relationships within the system.
Installation

Clone the repository:

Bash
git clone https://github.com/your-username/document-qa-system.git
Use code with caution.
content_copy
Install dependencies:

Bash
pip install -r requirements.txt
Use code with caution.
content_copy
Download the pre-trained BERT model and tokenizer (replace with download instructions). Save them as bert_model.pkl and bert_tokenizer.pkl in the project directory.

Run the Flask application:

Bash
python app.py
Use code with caution.
content_copy
Access the web interface: http://localhost:5000 in your browser.

Contributing

We welcome contributions! If you find issues or have suggestions, please open an issue or submit a pull request.

License

This project is licensed under the MIT License.