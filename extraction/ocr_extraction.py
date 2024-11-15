import easyocr

def extract_text_from_image(image_path):
    # Initialize EasyOCR reader
    reader = easyocr.Reader(['en', 'hi'],gpu=True)  # Supports English and Hindi
    result = reader.readtext(image_path)

    # Extract the text from the results
    extracted_text = " ".join([text[1] for text in result])
    return extracted_text
