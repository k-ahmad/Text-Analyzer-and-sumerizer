import string

def clean_text(text):
    text = text.lower()

    for char in string.punctuation:
        text = text.replace(char,"")

    return text