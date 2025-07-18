import requests
import streamlit as st

API_KEY = st.secrets['ASSEMBLYAI_API_KEY']
HEADERS = {'authorization': API_KEY}

def upload_file(audio_file):
    st.info('Envoi du fichier en cours...')
    response = requests.post('https://api.assemblyai.com/v2/upload', headers=HEADERS, data=audio_file)
    audio_url = response.json()['upload_url']
    st.success('Fichier envoyé')
    return get_transcript(audio_url)

def get_transcript(audio_url):
    st.info('Transcription en cours...')
    transcript_response = requests.post(
        'https://api.assemblyai.com/v2/transcript',
        json={'audio_url': audio_url, 'speaker_labels': True, 'auto_chapters': True},
        headers=HEADERS
    )
    transcript_id = transcript_response.json()['id']
    polling_endpoint = f'https://api.assemblyai.com/v2/transcript/{transcript_id}'
    while True:
        polling_response = requests.get(polling_endpoint, headers=HEADERS)
        status = polling_response.json()['status']
        if status == 'completed':
            return polling_response.json()['text']
        elif status == 'failed':
            return 'Échec de la transcription.'
        st.write('Traitement en cours...')
        st.sleep(3)

def record_audio():
    st.warning('Fonction d\'enregistrement à implémenter')
    return None
