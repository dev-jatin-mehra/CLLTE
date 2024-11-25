# from transformers import pipeline

# def summarize_text(text):
#     summarizer = pipeline("summarization")
#     return summarizer(text,max_length=130,min_length=30,do_sample=False)[0]["summary_text"]


# from sumy.parsers.plaintext import PlaintextParser
# from sumy.nlp.tokenizers import Tokenizer
# from sumy.summarizers.lex_rank import LexRankSummarizer

# def summarize_text(text):
#     parser = PlaintextParser.from_string(text, Tokenizer("english"))
#     summarizer = LexRankSummarizer()
#     summary = summarizer(parser.document, sentences_count=3)
#     return " ".join([str(sentence) for sentence in summary])

from transformers import pipeline # type: ignore

def summarize_text(text):
    summarizer = pipeline("summarization")
    return summarizer(text,max_length=530,min_length=130,do_sample=False)[0]["summary_text"]

