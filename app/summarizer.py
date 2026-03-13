import re

def split_sentences(text:str):
    sentences = re.split(r'(?<=[.!?])\s+',text)
    return [sentence.strip() for sentence in sentences if sentence.strip()]


def generate_summary(text:str,max_sentences:int =3) ->str:
    sentences = split_sentences(text)
    summary_sentences = sentences[:max_sentences]
    return " ".join(summary_sentences)

def extract_key_points(text:str,max_points:int=5):
    sentences = split_sentences(text)
    key_points = sentences[:max_points]
    return key_points