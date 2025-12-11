import os
import json

FILE_NAME = "saved_passwords.json"

def save_password(password):
    """Save password to a JSON file"""
    passwords = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            passwords = json.load(f)
    passwords.append(password)
    with open(FILE_NAME, "w") as f:
        json.dump(passwords, f, indent=4)
