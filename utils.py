import re
import string

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'https?://\S+', '', text)  # remove URLs
    text = re.sub(r'@\w+', '', text)          # remove mentions
    text = re.sub(r'#\w+', '', text)          # remove hashtags
    text = re.sub(r'\d+', '', text)           # remove numbers
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text.strip()
