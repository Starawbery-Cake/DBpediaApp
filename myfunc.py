import re

def extract_first_number(text:str) -> int:
    match = re.search(r'\d+', text)
    if match:
        return int(match.group())
    return None

def insert_newlines(text, interval=35):
    lines = [text[i:i+interval] for i in range(0, len(text), interval)]
    return '\n'.join(lines)