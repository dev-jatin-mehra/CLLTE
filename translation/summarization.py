from transformers import pipeline # type: ignore

def summarize_text(text):
    summarizer = pipeline("summarization")
    return summarizer(text,max_length=530,min_length=130,do_sample=False)[0]["summary_text"]