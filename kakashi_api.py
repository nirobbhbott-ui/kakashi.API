from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.responses import FileResponse
import subprocess
import tempfile

app = FastAPI(title="GoatBot Kakashi TTS API")

VOICEVOX_CLI = "./voicevox_linux_nvidia/voicevox_cli"
SPEAKER_ID = 3  # Kakashi

class TTSRequest(BaseModel):
    text: str

@app.post("/tts")
def text_to_speech(request: TTSRequest):
    text = request.text.strip()
    if not text:
        raise HTTPException(status_code=400, detail="Text is empty.")

    tmp_wav = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
    tmp_wav.close()
    output_file = tmp_wav.name

    try:
        subprocess.run(
            [VOICEVOX_CLI, "--text", text, "--speaker", str(SPEAKER_ID), "--out", output_file],
            check=True
        )
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=f"VOICEVOX error: {e}")

    return FileResponse(output_file, media_type="audio/wav", filename="kakashi.wav")
