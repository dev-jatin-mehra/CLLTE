from transformers import pipeline  # type: ignore
from translation.translation import translate_text

summarizer = pipeline("summarization")

def summarize_text(text, summary_length="medium", language_code="en"):
    length_config = {
        "short": {"max_length": 70, "min_length": 20},
        "medium": {"max_length": 200, "min_length": 70},
        "long": {"max_length": 350, "min_length": 200},
    }

    if summary_length not in length_config:
        raise ValueError("Invalid summary length option. Choose 'short', 'medium', or 'long'.")
    
    if language_code != "en":
        text = translate_text(text, "en")
    
    config = length_config[summary_length]
    summarized_text = summarizer(
        text, max_length=config["max_length"], min_length=config["min_length"], do_sample=False
    )[0]["summary_text"]
    
    if language_code != "en":
        summarized_text = translate_text(summarized_text, language_code)  # Translate back to target language

    return summarized_text