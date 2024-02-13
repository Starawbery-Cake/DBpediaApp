import re

def extract_first_number(text):
    match = re.search(r'\d+', text)
    if match:
        return int(match.group())
    return None