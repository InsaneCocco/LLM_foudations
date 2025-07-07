# Extract text from pdf and split into sentences
# Import necessary libraries
import fitz # PyMuPDF
import re


words=[]
# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page_num in range(doc.page_count):
        page = doc[page_num]
        text += page.get_text()
    doc.close()
    return text

# Function to split text into sentences using NLTK
def split_into_words(text):
    words.extend(re.findall(r'\b\w+\b', text))
    return words


pdf_path = 'mydocument.docx'
text = extract_text_from_pdf(pdf_path)
# print("Extracted Text:",text)
words_list = split_into_words(text)
# Print the extracted words
print("Words in the PDF:", words_list, '\n')
print(f'Number of words: {len(words_list)}')

