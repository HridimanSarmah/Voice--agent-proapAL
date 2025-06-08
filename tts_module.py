import requests
import os

def text_to_speech(text):
    headers = {
        "xi-api-key": os.getenv("ELEVENLABS_API_KEY"),
        "Content-Type": "application/json"
    }
    payload = {
        "text": text,
        "voice_settings": {"stability": 0.5, "similarity_boost": 0.5}
    }
    response = requests.post("https://api.elevenlabs.io/v1/text-to-speech/voice-id", headers=headers, json=payload)
    with open("response.mp3", "wb") as f:
        f.write(response.content)
