import easyocr
from PIL import Image
import streamlit as st
import cv2
import numpy as np
import random
# Dictionary mapping languages to their EasyOCR codes
supported_languages = {
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Italian": "it",
    "Dutch": "nl",
    "Portuguese": "pt",
    "Russian": "ru",
    "Arabic": "ar",
    "Chinese (Simplified)": "ch_sim",
    "Chinese (Traditional)": "ch_tra",
    "Japanese": "ja",
    "Korean": "ko",
    "Hindi": "hi",
    "Bengali": "ben",
    "Tamil": "ta",
    "Telugu": "te",
    "Malayalam": "ml",
    "Kannada": "kn",
    "Gujarati": "gu",
    "Punjabi": "pa",
    "Marathi": "mr",
    "Urdu": "ur",
    "Greek": "el",
    "Turkish": "tr",
    "Polish": "pl",
    "Ukrainian": "uk",
    "Vietnamese": "vi",
    "Thai": "th",
    "Czech": "cs",
    "Swedish": "sv",
    "Danish": "da",
    "Finnish": "fi",
    "Norwegian": "no",
    "Hungarian": "hu",
    "Romanian": "ro",
    "Slovak": "sk",
    "Croatian": "hr",
    "Serbian (Cyrillic)": "sr_cyrl",
    "Serbian (Latin)": "sr_lat",
    "Bulgarian": "bg",
    "Lithuanian": "lt",
    "Latvian": "lv",
    "Estonian": "et",
    "Icelandic": "is",
    "Swahili": "sw",
    "Filipino": "fil",
    "Hebrew": "he",
    "Georgian": "ka",
    "Nepali": "ne",
    "Sinhala": "si",
    "Pashto": "ps",
    "Kazakh": "kk",
    "Tajik": "tg",
    "Armenian": "hy",
    "Mongolian": "mn",
    "Malay": "ms",
    "Indonesian": "id",
    "Esperanto": "eo",
    "Haitian Creole": "ht",
    "Albanian": "sq",
    "Slovenian": "sl",
    "Belarusian": "be",
    "Yiddish": "yi"
}

# Define a function to generate random colors
def random_color():
    return [random.randint(0, 255) for _ in range(3)]

def extract_text_from_image(image_input, languages):

    st.write(languages)

    if not languages:
        raise ValueError(
            "No valid languages selected. Please choose from: " + ", ".join(supported_languages.keys())
        )

    # Initialize EasyOCR reader with selected languages
    reader = easyocr.Reader(languages, gpu=True)
    # Handle input types
    image = Image.open(image_input)
    image_source = cv2.cvtColor(np.array(image),cv2.COLOR_RGB2BGR)
    # Perform OCR on the image
    result = reader.readtext(image_source)

    for text in result:
        top_left = tuple(map(int,text[0][0]))
        bottom_right = tuple(map(int,text[0][2]))
        text_one = text[1]
        box_color = random_color()
        text_color = random_color()
        image_source = cv2.rectangle(image_source,top_left,bottom_right,box_color,5)
        image_source = cv2.putText(image_source,text_one,top_left,cv2.FONT_HERSHEY_SIMPLEX,1,text_color,2,cv2.LINE_AA)

    st.image(image_source,caption='Processed Image With Color Coded Text',use_container_width=False)
    extracted_text = " ".join([text[1] for text in result])
    return extracted_text

