# Kakashi TTS API

Converts text to Kakashi voice using VOICEVOX and exposes a FastAPI endpoint.

## Install
1. Install VOICEVOX: `bash install_voicevox.sh`
2. Install Python dependencies: `pip install -r requirements.txt`

## Run API
```bash
uvicorn kakashi_api:app --reload --host 0.0.0.0 --port 8000
