import requests

API_URL = "http://localhost:8000/tts"

def goatbot_speak(text: str, output_file: str = "kakashi.wav"):
    response = requests.post(API_URL, json={"text": text}, stream=True)
    if response.status_code == 200:
        with open(output_file, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"[GoatBot] Audio saved to {output_file}")
    else:
        print(f"[GoatBot] Error: {response.json()}")

if __name__ == "__main__":
    text = input("Enter text for Kakashi: ")
    goatbot_speak(text)
