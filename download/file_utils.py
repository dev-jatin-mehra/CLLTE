import tempfile

def save_to_text_file(text):
    with tempfile.NamedTemporaryFile(delete=False, mode='w', suffix='.txt',encoding='utf-8') as temp_file:
        temp_file.write(text)
        temp_file.seek(0)
        return temp_file.name

