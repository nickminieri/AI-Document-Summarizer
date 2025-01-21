# This code provided will take text that in inputted and summarize it

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

# Loop to ensure the user provides valid input
while True:
    # Prompting the user to choose between summarizing a file or pasting text
    choice = input("Do you want to summarize a file or paste text? Type 'file' or 'text': ").strip().lower()

    # Check if the input is valid
    if choice == "file":
        # Handle file input
        file_path = input("Enter the path to your file: ").strip()
        
        # Check if the file exists
        if os.path.exists(file_path):
            # Read the file content
            with open(file_path, 'r') as file:
                content = file.read()
            print("File content loaded successfully!")
            
            # Summarize the file content
            summary = summarizer(content, max_length=50, min_length=25, do_sample=False)
            print("Summary:", summary[0]['summary_text'])
            break  # Exit the loop once done
        else:
            # If the file doesn't exist, inform the user
            print("File not found. Please check the path.")
    elif choice == "text":
        # Handle pasted text input
        text = input("Enter the text you want to summarize: ").strip()
        
        # Summarize the text
        summary = summarizer(text, max_length=50, min_length=25, do_sample=False)
        print("Summary:", summary[0]['summary_text'])
        break  # Exit the loop once done
    else:
        # Inform the user of invalid input and loop back
        print("Invalid choice. Please type 'file' or 'text'.")