from transformers import pipeline

def summarize_text(text):
    summarizer = pipeline("summarization")
    return summarizer