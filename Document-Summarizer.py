# This code provided will take text that in inputted and summarize it

import os

# Steps for Your Program:
# 1. Prompting the user to ask option they would like
choice = input("Do you want to summarize a file or pate text? Type 'file' or 'text': ")
print("You choose:", choice) # telling the user what they choose

if choice == "file":
    file_path = input("Enter the path to your file: ")
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            content = file.read()
            print("File content loaded successfully!")
    else:
        print("File not found. Please check the path.")
if choice == 'text':
#Summarize the Text and # 5. Output the Summary:
    from transformers import pipeline
    summarizer = pipeline("summarization") # create a summarizer
    text = input("Enter the text you want to be summarized: ")
    summary = summarizer(text, max_length=50, min_length=25, do_sample=False)
    print("Summary:", summary[0]['summary_text'])
else:
    print("Input not found")