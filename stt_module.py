import requests
import os

def transcribe_audio(audio_url):
    headers = {
        "Authorization": f"Token {os.getenv('DEEPGRAM_API_KEY')}"
    }
    response = requests.post(
        "https://api.deepgram.com/v1/listen",
        headers=headers,
        data=requests.get(audio_url).content
    )
    return response.json()['results']['channels'][0]['alternatives'][0]['transcript']
