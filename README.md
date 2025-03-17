# Token Counter

This script counts the number of tokens and words in a PDF file using OpenAI's tiktoken library for tokenization.

## Requirements

- Python 3.x
- PyPDF2
- tiktoken

You can install the required packages using pip:

```bash
pip install -r requirements.txt
```

## Usage

Run the script and follow the prompt to enter the path to the PDF file:

```bash
python token_counter.py
```

The script will prompt you to enter the path to the PDF file:

```
Please enter the path to the PDF file:
```

After entering the path, the script will output the token count and word count of the specified PDF file.

## Example

```
Please enter the path to the PDF file: example.pdf
Token count: 1234
Word count: 567
```
