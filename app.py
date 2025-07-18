import streamlit as st
from utils import record_audio, upload_file, get_transcript

st.title('Verbatim - Compte-rendu simplifié')

st.write('Choisissez une option :')

option = st.radio('Mode', ('🎙️ Enregistrer une réunion', '📁 Uploader un enregistrement'))

if option == '🎙️ Enregistrer une réunion':
    if st.button('Démarrer l\'enregistrement'):
        audio_file = record_audio()
        transcript = upload_file(audio_file)
        st.text_area('Transcription', transcript, height=300)
elif option == '📁 Uploader un enregistrement':
    uploaded_file = st.file_uploader('Uploader un fichier audio', type=['mp3', 'wav'])
    if uploaded_file and st.button('Envoyer pour transcription'):
        transcript = upload_file(uploaded_file)
        st.text_area('Transcription', transcript, height=300)
