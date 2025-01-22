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
# 3. Modularity:
    # Try breaking the code into smaller functions. 
    # For example:
        # A function for summarizing text.
        # A function for handling file input.
        # A main function to run the program.

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

            # Summarize the file content
                summary = summarizer(content, max_length=50, min_length=25, do_sample=False)
                print("Summary:", summary[0]['summary_text'])
                break  # Exit the loop once done
        
            except Exception as e:
                print(f"An error occurred while reading the file: {e}")
            
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