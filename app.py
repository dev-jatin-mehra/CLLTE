import os 
import streamlit as st
from extraction.ocr_extraction import extract_text_from_image, supported_languages
from extraction.pdf_extraction import extract_text_from_pdf
from extraction.audio_extraction import extract_text_from_audio
# from video_extraction import extract_text_from_video
# from translation import translate_text
# from summarization import summarize_text
from processing.text_cleanup import reorder_text
# from file_utils import save_to_text_file, save_to_pdf, save_to_audio
from PIL import Image
from googletrans import LANGUAGES
from translation.translation import translate_text

#set page configuration
st.set_page_config(
    page_title="Cross-Lingual Text Tool",
    page_icon="🌐",
    layout='wide',
    initial_sidebar_state="collapsed",
)

#sidebar 
st.sidebar.image(image="assets/logo.jpg",width=50,channels="BGR")
st.sidebar.title(body="Cross-Lingual Text Tool")
st.sidebar.markdown(body="<h3>Easily extract, translate, summarize and convert to text/audio</h3><hr>",
                    help="@2024",unsafe_allow_html=True)

#Main UI
st.title("🌍 Cross-Lingual Text Extraction, Translation, and Summarization",)
st.markdown("**Upload a file or use live input to extract text, translate it, summarize it, and even generate audio.**")
file_type=""
#Tabs
tabs = st.tabs(["📤 Input", "📝 Processing", "🔊 Outputs"])
extracted_text=""
#Tab:1
with tabs[0]:
    st.header("Input Section")
    input_type = st.radio("Choose input type:",["Nothing","File Upload","Live Voice Input"])

    if input_type=="File Upload":
        file_type = st.selectbox("Select File Type:",["None","Image","PDF","Audio","Video"])
        if file_type=="Image":
            uploaded_file = st.file_uploader("Upload Your File:",type=["jpg","jpeg","png"])
            if uploaded_file:
                # Get file extension
                file_extension = os.path.splitext(uploaded_file.name)[1].lower()
                #CHECK
                if file_extension not in [".jpg", ".jpeg", ".png"]:
                    st.error("Invalid file type! Please upload an image file with .jpg, .jpeg, or .png extension.")
                else:
                    language_choice = st.selectbox("Select OCR language", list(supported_languages.keys()))
                    lang_code = []
                    lang_code.append(supported_languages[language_choice])
                    image = Image.open(uploaded_file)
                    st.image(image, caption="Uploaded Image", use_container_width=False)
                    extracted_text = extract_text_from_image(uploaded_file, lang_code)
                    st.write(extracted_text)
                    

        elif file_type=="PDF":
            uploaded_file = st.file_uploader("Upload Your File:",type=["pdf"])
            if uploaded_file:
                # Get file extension
                file_extension = os.path.splitext(uploaded_file.name)[1].lower()
                #CHECK
                if file_extension not in [".pdf"]:
                    st.error("Invalid file type! Please upload a pdf file with .pdf extension")
                else:
                    extracted_text = extract_text_from_pdf(uploaded_file)
                    st.write(extracted_text)
                    


        elif file_type=="Audio":
            uploaded_file = st.file_uploader("Upload Your File:",type=["mp3","wav",".m4a",".aac",".flac"])
            if uploaded_file:
                file_extension = os.path.splitext(uploaded_file.name)[1].lower()
                #CHECK
                if file_extension not in [".mp3",".wav",".m4a",".aac",".flac"]:
                    st.error("Invalid file type! Please upload a audio file with .mp3, .wav, .aac, .flac or .m4a extension")
                else:
                    extracted_text = extract_text_from_audio(uploaded_file)
                    st.write(extracted_text)
                    


        elif file_type=="Video":
            uploaded_file = st.file_uploader("Upload Your File:",type=["mp4"])
            if uploaded_file:
                file_extension = os.path.splitext(uploaded_file.name)[1].lower()
                #CHECK
                if file_extension not in [".mp4"]:
                    st.error("Invalid file type! Please upload a video file with .mp4 extension")
                else:
                    extracted_text = extract_text_from_audio(uploaded_file)
                    st.write(extracted_text)
    elif input_type=="Live Voice Input":
        st.write("Under Construction ! 😁")


#Tab:2
with tabs[1]:
    st.write("Will Start")
    st.subheader("Translate Text")
    language = st.selectbox("Select a language to translate into", options=list(LANGUAGES.values()))
    language_code = list(LANGUAGES.keys())[list(LANGUAGES.values()).index(language)]

    if st.button("Translate"):
        translated_text = translate_text(extracted_text, language_code)
        st.subheader("Translated Text")
        st.write(translated_text)



#tab:3
with tabs[2]:
    st.write("Will Start")