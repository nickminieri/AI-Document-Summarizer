# This code provided will take text that in inputted and summarize it

# things to add
# 1. prevent empty input:
    # for both file paths and text inputs, check if the user accidentally 
    # presses Enter without typing anything. add a condition to ensure 
    # the input isn’t empty.
# 2. Categorization for the Future:
    # Once the summarizer is working, explore automatically categorizing the 
    # text into topics (e.g., "science," "finance"). This could be the next 
    # logical extension to the project.

import os
from transformers import pipeline, logging
import warnings

# Suppress logs and warnings
logging.set_verbosity_error()
warnings.filterwarnings("ignore")
os.environ["PYTHONWARNINGS"] = "ignore"

# Create the summarization pipeline with the specified model
# Explicitly specifying the default model to avoid warnings
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def choose_file():
    print("Accepted file types: .txt")
    file_path = input("Enter the full path of the file (e.g., /Users/YourName/Desktop/yourfile.txt): ").strip()

    # Remove quotes if included accidentally
    if file_path.startswith("'") and file_path.endswith("'"):
        file_path = file_path[1:-1]
    elif file_path.startswith('"') and file_path.endswith('"'):
        file_path = file_path[1:-1]

    # Check if the file exists
    if os.path.isfile(file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                print("File content loaded successfully!")

                # Truncate content to the model's input limit (512 tokens for most models)
                truncated_content = content[:1024]
                summary = summarizer(truncated_content, max_length=50, min_length=25, do_sample=False)
                print("Summary:", summary[0]['summary_text'])

        except Exception as e:
            print(f"An error occurred while reading the file: {e}")
    else:
        print("File not found. Please check the path.")

def choose_text():
    text = input("Enter the text you want to summarize: ").strip()

    # Truncate text to the model's input limit (512 tokens for most models)
    truncated_text = text[:1024]
    summary = summarizer(truncated_text, max_length=50, min_length=25, do_sample=False)
    print("Summary:", summary[0]['summary_text'])

if __name__ == "__main__":
    # Loop to ensure the user provides valid input
    while True:
        # Prompting the user to choose between summarizing a file or pasting text
        choice = input("Do you want to summarize a file or paste text? Type 'file', 'text', or 'exit': ").strip().lower()

        if choice == "file":
            choose_file()
        elif choice == "text":
            choose_text()
        elif choice == "exit":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please type 'file', 'text', or 'exit'.")
