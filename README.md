# Major-Project
Code,Documents,Reference,Source for Major Project 2024 Batch.

Title
Document Question Answering using NLP Techniques.


Link for resources-- BERT<[text](https://towardsdatascience.com/bert-explained-state-of-the-art-language-model-for-nlp-f8b21a9b6270)>

# Document Question Answering System using NLP Techniques

This is a Flask web application that allows users to upload PDF files and ask questions related to the content of those files. The system utilizes the BERT (Bidirectional Encoder Representations from Transformers) model for question answering and combines natural language processing techniques with deep learning to provide accurate answers.

## Features

- Upload PDF files to the system
- Ask questions related to the uploaded PDF content
- Get answers extracted from the PDF using the fine-tuned BERT model
- Handle long-form documents by intelligently splitting and preserving context
- Display the answer along with relevant context from the PDF
- Web-based interface for easy accessibility

## Architecture

The system follows a client-server architecture with a Flask backend and a web-based frontend. The core components of the system include:

1. **BERT Model**: The fine-tuned BERT model is responsible for converting questions and document content into semantic representations, enabling accurate answer identification.

2. **Document Processing**: The system employs an "expand_split_sentences" function to handle long documents exceeding BERT's token limit. This function intelligently splits paragraphs into smaller segments while preserving the overall context.

3. **Answer Extraction**: The system combines extractive and abstractive summarization techniques to generate concise and informative responses from the relevant document passages.

4. **Web Interface**: The Flask backend serves a user-friendly web interface, allowing users to upload PDF files, enter questions, and view the extracted answers with relevant context.

### BERT Architecture

The BERT (Bidirectional Encoder Representations from Transformers) model is a powerful language representation model that forms the core of the question answering system. Here's an overview of its architecture:

- **Input Embeddings**: The input tokens are mapped to their corresponding embeddings (word, position, and segment embeddings) to create the initial input representations.
- **Multi-Head Attention**: The model applies multi-head self-attention mechanisms to capture the contextual relationships between words in the input sequence.
- **Feed-Forward Networks**: The output from the attention layer is passed through feed-forward networks to further process and refine the representations.
- **Encoder Layers**: Multiple encoder layers, each consisting of multi-head attention and feed-forward networks, are stacked to build deep representations of the input.
- **Output Representations**: The final output representations from the BERT encoder are used for various downstream tasks, such as question answering, text classification, and language generation.

## System Design

The project follows a well-defined system design, as illustrated in the UML diagrams and sequence diagrams provided in the Major Project PPT file. Key components include:

- **Use Case Diagram**: Depicts the interactions between users and the system, highlighting the main use cases like uploading PDF files, asking questions, and viewing answers.
- **Sequence Diagrams**: Illustrates the sequence of interactions between objects or components within the system, such as handling file uploads, processing questions, and rendering responses.
- **Flowchart**: Represents the flow of operations and decision points within the system, providing a visual representation of the program's execution.
- **ER Diagram**: Depicts the data entities and their relationships within the system, if applicable.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/document-qa-system.git

Install the required dependencies:

pip install -r requirements.txt

Download the pre-trained BERT model and tokenizer, and save them as bert_model.pkl and bert_tokenizer.pkl in the project directory.

Run the Flask application:

bashCopy codepython app.py

Access the web interface by opening your browser and navigating to http://localhost:5000.

Contributing
Contributions to this project are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.
License
This project is licensed under the MIT License.
