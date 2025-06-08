import time
from datetime import datetime
from stt_module import transcribe_audio
from llm_module import generate_response
from tts_module import text_to_speech
from metrics_logger import log_metrics

def process_conversation(audio_url):
    start = time.time()

    stt_start = time.time()
    text = transcribe_audio(audio_url)
    stt_latency = time.time() - stt_start

    llm_start = time.time()
    reply = generate_response(text)
    llm_latency = time.time() - llm_start

    tts_start = time.time()
    text_to_speech(reply)
    tts_latency = time.time() - tts_start

    total_latency = time.time() - start

    log_metrics({
        "timestamp": datetime.now(),
        "EOU Delay": stt_latency,
        "TTFT": llm_latency,
        "TTFB": tts_latency,
        "Total Latency": total_latency,
        "User Input": text,
        "Response": reply
    })

# Example usage
if __name__ == "__main__":
    process_conversation("https://example.com/sample_audio.wav")
