# Don't judge the code i have 0 fucking clue what im doing. Thanks google and stackoverflow and a little bit of reddit

import os
import pickle
from core.state import character

SAVE_DIR = "Therostia Saves"

def ensure_saves_dir():
    if not os.path.exists(SAVE_DIR):
        os.makedirs(SAVE_DIR)

def list_save_files():
    ensure_saves_dir()
    return [f for f in os.listdir(SAVE_DIR) if f.endswith('.pkl')]

def format_filename(char):
    safe_name = char.name.strip().replace(" ", "_")
    return f"{safe_name}_Lv{char.level}_HP{char.health}_XP{char.XP}.pkl"

def save_character(char, filename=None):
    ensure_saves_dir()
    if not filename:
        filename = format_filename(char)

    path = os.path.join(SAVE_DIR, filename)
    with open(path, "wb") as f:
        pickle.dump(char, f)

    print(f"💾 Game saved to {path}")

def load_character():
    ensure_saves_dir()
    files = list_save_files()

    if not files:
        print("❌ No save files found.")
        return None

    print("📂 Available Saves:")
    for i, f in enumerate(files):
        print(f"{i + 1}) {f}")

    try:
        choice = int(input("Select save number: "))
        if 1 <= choice <= len(files):
            path = os.path.join(SAVE_DIR, files[choice - 1])
            with open(path, "rb") as f:
                loaded_char = pickle.load(f)
            print("✅ Save loaded successfully!")
            return loaded_char
        else:
            print("❌ Invalid selection.")
            return None
    except ValueError:
        print("❌ Invalid input.")
        return None
