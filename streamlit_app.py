import time
import streamlit as st
from src.transcriber import AudioToText

st.set_page_config(
    page_title="🔉Audio to Text💬",
    page_icon="🔉"
)


with st.sidebar:
    st.title(
        "🔉Audio to Text💬 convertor"
    )
    st.markdown("""
    ## Overview
    * The "Audio to Text Transcription with [AssemblyAI](https://www.assemblyai.com/) and [Streamlit](https://streamlit.io/)" project is a web application that allows users to upload audio files and convert them into text using the AssemblyAI API. This project demonstrates the integration of AssemblyAI's powerful speech-to-text capabilities with the interactive features of Streamlit, a popular framework for creating data applications in Python.

    ## Objectives
    * **User-Friendly Interface**: Provide a simple and intuitive web interface for users to upload audio files and receive transcriptions.
    * **Real-Time Transcription**: Utilize AssemblyAI's API to convert audio to text in real-time.
    * **Interactive Features**: Allow users to play the uploaded audio file within the application and view the transcription results.

    ## Key Features
    * **Audio File Upload**: Users can upload audio files in various formats including WAV, MP3, and M4A.
    * **API Integration**: Seamless integration with AssemblyAI API for uploading audio files and fetching transcription results.
    * **Real-Time Feedback**: Display a progress spinner while the transcription is being processed and show the transcription result once completed.
    * **Audio Playback**: Allow users to play the uploaded audio file directly in the application.
    * **Error Handling**: Provide appropriate feedback in case of transcription failures.
""")

api_key = st.text_input('Enter your AssemblyAI API key', placeholder="ASSEMBLYAI_API_KEY", type="password")
st.write("Sign Up and Get an API Key: [AssemblyAI API Key](https://www.assemblyai.com/app)")
uploaded_file = st.file_uploader(
    'Choose an audio file', type=['wav', 'mp3', 'm4a'])


if uploaded_file is not None and api_key:
    st.audio(uploaded_file, format='audio/wav')

    if st.button('Transcribe'):
        with st.spinner('Transcribing...'):
            transcription = AudioToText.transcribe_audio(
                uploaded_file, api_key)
            st.text_area('Transcription', transcription, height=400)
            st.download_button(
                label="Download .txt file",
                data=transcription,
                file_name="transcriber.txt",
                mime="text/plain"
            )
