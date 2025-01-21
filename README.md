# AI Document Summarizer

## Overview
The AI Document Summarizer is a Python-based tool designed to make text summarization simple and efficient. It allows users to either summarize the contents of a file or directly summarize text input. This project utilizes the Hugging Face Transformers library for natural language processing.

## Features
- Summarize text from a file.
- Summarize directly pasted text.
- Easy-to-use input prompts for selecting options.
- Powered by state-of-the-art NLP models from Hugging Face.

## How It Works
1. **User Choice**: The program prompts the user to choose between summarizing a file or directly entering text.
2. **File Summarization**: If the file option is chosen, the user provides a file path. The program reads the file and summarizes its content.
3. **Text Summarization**: If the text option is chosen, the user pastes the text they want summarized.
4. **Output**: The summarized text is printed directly to the console.

## Getting Started

### Prerequisites
- Python 3.10 or higher
- Required libraries:
  - `transformers`
  - `torch`
  - `os` (built-in)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/AI-Document-Summarizer.git
2. Navigate to the project directory:
   ```bash
   cd AI-Document-Summarizer
3. Install the required libraries:
   ```bash
   pip install transformers torch

### Running the Program
1. Navigate to the project directory.
2. Run the program:
   ```bash
   python3 main.py
3. Follow the on-screen prompts to summarize a file or text.

### Future Enhancements
- Add text categorization to classify documents into topics like "science," "finance," etc.
- Enable saving summarized output to a new file.
- Improve error handling and user input validation.

###Contributions
Contributions are **welcome**! Feel free to fork the repository, create a new branch, and submit a pull request.

