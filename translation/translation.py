from googletrans import Translator

def translate_text(text, target_language):

    if not text.strip():
        return "Error: No text provided for translation."
    
    translator = Translator()
    try:
        translated = translator.translate(text, dest=target_language)
        return translated.text
    except Exception as e:
        return f"Error during translation: {e}"
