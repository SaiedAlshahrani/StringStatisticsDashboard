from transformers import AutoTokenizer

def count_string_tokens(text):
    tokenizer = AutoTokenizer.from_pretrained("humain-ai/ALLaM-7B-Instruct-preview")
    tokens = tokenizer.tokenize(text, use_fast=False)
    num_tokens = len(tokens)
    return num_tokens

def get_string_length_counts(text):
    char_count = len(text)
    word_count = len(text.split())
    parag_count = sum(1 for p in text.split('\n') if p.strip())
    return char_count, word_count, parag_count
