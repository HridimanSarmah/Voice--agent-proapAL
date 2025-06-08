# AI Voice Agent – proPAL AI Internship Project

## 🔧 Description
This project implements a simple real-time AI voice agent pipeline using:
- LiveKit (for audio stream)
- Deepgram (STT)
- OpenAI (LLM)
- ElevenLabs (TTS)

## 📂 Structure
- `app.py`: Main controller
- `stt_module.py`: Speech-to-text
- `llm_module.py`: Text generation
- `tts_module.py`: Text-to-speech
- `metrics_logger.py`: Excel metrics logger
- `.env`: Store your API keys here

## 🚀 How to Run
1. Clone this repo and install dependencies:
```bash
pip install -r requirements.txt
```

2. Fill in your `.env` with the required API keys.

3. Run the app:
```bash
python app.py
```

## 📊 Metrics Logged
- EOU Delay
- TTFT
- TTFB
- Total Latency
- User Input / Response

## 📌 Note
Replace the test audio URL in `app.py` with an actual WAV/MP3 file URL.

## 🕒 Submission
Deadline: 8 PM, 10th June
