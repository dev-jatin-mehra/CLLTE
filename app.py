import os 
import streamlit as st  # type: ignore
import speech_recognition as sr  # type: ignore
from extraction.ocr_extraction import extract_text_from_image, supported_languages
from extraction.pdf_extraction import extract_text_from_pdf
from extraction.audio_extraction import extract_text_from_audio
from extraction.video_extraction import extract_text_from_video
from translation.translation import translate_text
from translation.summarization import summarize_text
# from processing.text_cleanup import reorder_text
from download.file_utils import save_to_text_file, save_to_pdf
from processing.text_to_audio import save_to_audio
from PIL import Image
from googletrans import LANGUAGES  # type: ignore

# Accent options for gTTS
accent_options = {
    "English (US)": "en",
    "English (UK)": "en-uk",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Hindi": "hi",
    "Japanese": "ja",
}

# Set page configuration
st.set_page_config(
    page_title="Cross-Lingual Text Tool",
    page_icon="assets/main.png",
    layout='wide',
    initial_sidebar_state="collapsed",
)

# Sidebar 
st.sidebar.image(image="assets/main.png", width=100, channels="BGR")
st.sidebar.title(body="Cross-Lingual ETS")
st.sidebar.markdown(
    body="<h3>Easily extract, translate, summarize and convert to text/audio</h3><hr>",
    help="2024", unsafe_allow_html=True
)

# Initialize session states for translated and summarized text
if 'translated_text' not in st.session_state:
    st.session_state.translated_text = None  # Use None to represent uninitialized state
if 'summarized_text' not in st.session_state:
    st.session_state.summarized_text = None

# Main UI
st.title("🌍 Cross-Lingual Text Extraction, Translation, and Summarization")
st.markdown("**Upload a file or use live input to extract text, translate it, summarize it, and even generate audio.**")
file_type = ""
# Tabs
tabs = st.tabs(["📤 Input", "📝 Processing", "🔊 Outputs"])
extracted_text = ""

# Tab:1
with tabs[0]:
    st.header("Input Section")
    input_type = st.radio("Choose input type:", ["Nothing", "File Upload"])

    if input_type == "File Upload":
        file_type = st.selectbox("Select File Type:", ["None", "Image", "PDF", "Audio", "Video"])
        if file_type == "Image":
            uploaded_file = st.file_uploader("Upload Your File:", type=["jpg", "jpeg", "png"])
            if uploaded_file:
                file_extension = os.path.splitext(uploaded_file.name)[1].lower()
                if file_extension not in [".jpg", ".jpeg", ".png"]:
                    st.error("Invalid file type! Please upload an image file with .jpg, .jpeg, or .png extension.")
                else:
                    language_choice = st.selectbox("Select OCR language", list(supported_languages.keys()))
                    lang_code = [supported_languages[language_choice]]
                    image = Image.open(uploaded_file)
                    st.image(image, caption="Uploaded Image", use_container_width=False)
                    extracted_text = extract_text_from_image(uploaded_file, lang_code)
                    st.write(extracted_text)

        elif file_type == "PDF":
            uploaded_file = st.file_uploader("Upload Your File:", type=["pdf"])
            if uploaded_file:
                file_extension = os.path.splitext(uploaded_file.name)[1].lower()
                if file_extension != ".pdf":
                    st.error("Invalid file type! Please upload a PDF file.")
                else:
                    extracted_text = extract_text_from_pdf(uploaded_file)
                    st.write(extracted_text)

        elif file_type == "Audio":
            uploaded_file = st.file_uploader("Upload Your File:", type=["mp3", "wav", ".m4a", ".aac", ".flac"])
            if uploaded_file:
                file_extension = os.path.splitext(uploaded_file.name)[1].lower()
                if file_extension not in [".mp3", ".wav", ".m4a", ".aac", ".flac"]:
                    st.error("Invalid file type! Please upload a valid audio file.")
                else:
                    extracted_text = extract_text_from_audio(uploaded_file)
                    st.write(extracted_text)


        elif file_type == "Video":
                uploaded_file = st.file_uploader("Upload Your File:", type=["mp4"])
                if uploaded_file:
                    file_extension = os.path.splitext(uploaded_file.name)[1].lower()
                    if file_extension != ".mp4":
                        st.error("Invalid file type! Please upload a video file with .mp4 extension.")
                    else:
                        language = st.selectbox("Select Language for Speech Recognition", 
                                                ["English (en)", "Spanish (es)", "French (fr)", "German (de)", "Hindi (hi)", "Chinese (zh)"])
                        language_code = language.split("(")[-1].strip(")")
                        
                        st.info("Processing the video...")
                        extracted_text = extract_text_from_video(uploaded_file, language_code)
                        st.write("*Extracted Text:*")
                        st.write(extracted_text)

# Tab:2
with tabs[1]:
    trans_text = ""
    st.header("Processing Section")

    # Translate Text
    language = st.selectbox("Select a language to translate into", options=list(LANGUAGES.values()))
    language_code = list(LANGUAGES.keys())[list(LANGUAGES.values()).index(language)]

    if st.button("Translate"):
        trans_text=st.session_state.translated_text = translate_text(extracted_text, language_code)
        st.subheader("Translated Text")
        st.write(st.session_state.translated_text)

    # Summarize Text
    summary_length_option = st.selectbox("Select Summary Length:", ["short", "medium", "long"])
    if st.button("Summarize"):
        if summary_length_option:
            summarized_content=""
            if trans_text:
                summarized_content = summarize_text(trans_text,summary_length=summary_length_option)
            else:
                summarized_content = summarize_text(extracted_text,summary_length=summary_length_option)

            st.session_state.summarized_text = translate_text(summarized_content, language_code)
            st.subheader("Summarized Text")
            st.write(st.session_state.summarized_text)

# Tab:3
if extracted_text:
    with tabs[2]:
        st.header("Output Section")
        export_choice = st.selectbox("Choose Text To Download:", ["Translated Text", "Summarized Text"])

        if export_choice == "Translated Text" and st.session_state.translated_text:
            output_text = st.session_state.translated_text
        elif export_choice == "Summarized Text" and st.session_state.summarized_text:
            output_text = st.session_state.summarized_text
        else:
            st.error("Please complete the translation or summarization before downloading")
            output_text = None

        if output_text:
            download_format = st.selectbox("Choose Download Format:", ["Text File", "PDF", "Audio"])
            file_name = st.text_input("Enter file name (without extension):", value="output")

            if st.button("Download"):
                file_name = file_name.strip() or "output"

                if download_format == "Text File":
                    save_to_text_file(output_text, f"{file_name}.txt")
                    with open(f"{file_name}.txt", "rb") as file:
                        st.download_button("Download as text file", file, f"{file_name}.txt")

                elif download_format == "PDF":
                    save_to_pdf(output_text, f"{file_name}.pdf")
                    with open(f"{file_name}.pdf", "rb") as file:
                        st.download_button("Download as PDF", file, f"{file_name}.pdf")

                elif download_format == "Audio":
                    audio_file = save_to_audio(output_text, f"{file_name}.mp3", "en")
                    with open(audio_file, "rb") as file:
                        st.audio(file.read(), format="audio/mp3")
                        st.download_button("Download as Audio", file, f"{file_name}.mp3")

