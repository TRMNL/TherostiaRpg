import os
import pickle

SAVE_DIR = "Therostia Saves"

def ensure_saves_dir():
    if not os.path.exists(SAVE_DIR):
        os.makedirs(SAVE_DIR)

def list_save_files():
    ensure_saves_dir()
    return [f for f in os.listdir(SAVE_DIR) if f.endswith('.pkl')]

def save_character(character, filename="save1.pkl"):
    ensure_saves_dir()
    path = os.path.join(SAVE_DIR, filename)
    with open(path, "wb") as f:
        pickle.dump(character, f)
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
                character = pickle.load(f)
            print("✅ Save loaded successfully!")
            return character
        else:
            print("❌ Invalid selection.")
            return None
    except ValueError:
        print("❌ Invalid input.")
        return None
