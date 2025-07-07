# Import necessary libraries
import fitz # PyMuPDF
import nltk
from nltk.tokenize import sent_tokenize

# Download the Punkt tokenizer for sentence splitting
nltk.download('punkt_tab')
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
def split_into_sentences(text):
    sentences = sent_tokenize(text)
    return sentences


pdf_path = 'File_to_split'
text = extract_text_from_pdf(pdf_path)
# print("Extracted Text:",text)
sentences = split_into_sentences(text)
# Print the extracted sentences
for i, sentence in enumerate(sentences, 1):
    print(f"Sentence {i}: {sentence}")