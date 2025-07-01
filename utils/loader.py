import json
import random

def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def get_random_affirmation():
    data = load_json("content/affirmations.json")
    return random.choice(data)

def get_random_love_note():
    data = load_json("content/love_letters.json")
    return random.choice(data)

def get_proof_item():
    data = load_json("content/proof_log.json")
    return random.choice(data)

def get_emergency_message():
    with open("content/emergency_message.txt", "r", encoding="utf-8") as f:
        return f.read()
