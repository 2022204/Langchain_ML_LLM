# pip install PyPDF2


## pip install openai
## pip install faiss-cpu
## pip install langchain
import os
from PyPDF2 import PdfReader

location = r'C:/Users/ha170/OneDrive\Desktop/Langchain/'

input_file = input("Enter pdf file name (e.g Abc.pdf) " )
path = location + input_file
reader= PdfReader(path)

raw_text = ""
for i, page in enumerate(reader.pages):
    text = page.extract_text()
    if text:
        raw_text+=text
        
output_file, ext = os.path.splitext(input_file)

output_file += '.txt'
with open(output_file, 'w', encoding='utf-8') as file:
    file.write(raw_text)
