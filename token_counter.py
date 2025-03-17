import PyPDF2
import tiktoken


def read_pdf(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text

def count_tokens(text):
    enc = tiktoken.get_encoding("cl100k_base")  # This is GPT-4's tokenizer
    tokens = enc.encode(text)
    return len(tokens)

def count_words(text):
    words = text.split()
    return len(words)

if __name__ == "__main__":
    pdf_path = input("Please enter the path to the PDF file: ").strip().strip('"')
    
    text = read_pdf(pdf_path)
    token_count = count_tokens(text)
    word_count = count_words(text)
    print(f"Token count: {token_count}")
    print(f"Word count: {word_count}")
