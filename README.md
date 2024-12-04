# 🌍 Cross-Lingual Text Extraction, Translation, and Summarization

This project is a comprehensive tool for extracting text from various sources (images, PDFs, audio, and videos), translating it into multiple languages, summarizing it with customizable lengths, and providing options to download the output in various formats (text, PDF, or audio).

---

## Features

1. **Input Handling**

   - **Image, PDF, Audio, and Video**: Supports text extraction from various file types.
   - **Multi-Language OCR**: Detect and extract text in multiple languages.

2. **Text Processing**

   - Text structure reordering for improved readability.
   - Translation into multiple languages with Google Translate API.
   - Summarization with customizable lengths (short, intermediate, long).

3. **Output Options**
   - Download translated or summarized text as:
     - **Text File (.txt)**
     - **PDF File (.pdf)**
     - **Audio File (.mp3)** with support for accent selection(us,uk,au,ca).

---

## Installation

### Prerequisites

- **Python 3.8+**
- Required Python libraries (installed via `requirements.txt`)

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/cross-lingual-text-tool.git
   cd cross-lingual-text-tool
   ```
2. Create and Activate the virtual Environment
   ```bash
   python -m venv <name the venv>
   source <venv name>/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install Dependencies
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application
   ```bash
   streamlit run app.py
   ```

## Project Structure

    ```bash
    cross-lingual-text-tool/
    ├── app.py                # Main Streamlit app
    ├── requirements.txt      # Dependencies
    ├── README.md             # Project documentation
    ├── extraction/           # Text extraction modules
    │   ├── ocr_extraction.py
    │   ├── pdf_extraction.py
    │   ├── audio_extraction.py
    │   ├── video_extraction.py
    ├── translation/          # Translation and summarization
    │   ├── translation.py
    │   ├── summarization.py
    ├── processing/           # Text cleanup and audio conversion
    │   ├── text_cleanup.py
    │   ├── text_to_audio.py
    ├── download/             # File download utilities
    │   ├── file_utils.py
    ├── assets/               # Static assets like images
    ├── github.bat            # batch file for git push
    ├── gitpull.bat           # bacth file for git pull
    ├── LICENSE.md            # MIT license

## Future Enhancements

- Support for more OCR engines (e.g., Amazon Textract, PaddleOCR).
- Advanced summarization models.
- Enhanced UI for real-time translation feedback.

## Credits

- **Frameworks & Libraries**: Streamlit, Easy OCR, Google Translator, BART, gTTS.
- **Developed By**: Jatin/[Dinesh](https://example.com)

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.
