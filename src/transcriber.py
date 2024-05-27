import streamlit as st
import requests
import time


class AudioToText:
    def transcribe_audio(file, api_key):
        headers = {
            'authorization': api_key,
            'content-type': 'application/json'
        }

        # Upload the audio file
        upload_response = requests.post(
            'https://api.assemblyai.com/v2/upload',
            headers=headers,
            files={'file': file}
        )

        audio_url = upload_response.json()['upload_url']

        # Request transcription
        transcription_request = {
            'audio_url': audio_url
        }

        transcribe_response = requests.post(
            'https://api.assemblyai.com/v2/transcript',
            json=transcription_request,
            headers=headers
        )

        transcript_id = transcribe_response.json()['id']

        # Polling for the transcription result
        while True:
            transcript_response = requests.get(
                f'https://api.assemblyai.com/v2/transcript/{transcript_id}',
                headers=headers
            )

            transcript = transcript_response.json()

            if transcript['status'] == 'completed':
                return transcript['text']
            elif transcript['status'] == 'failed':
                return 'Transcription failed.'
            else:
                time.sleep(5)