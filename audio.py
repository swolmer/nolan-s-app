from playsound import playsound
import os

def play_voice(name):
    path = f"assets/voice_memos/{name}.mp3"
    if os.path.exists(path):
        playsound(path)
