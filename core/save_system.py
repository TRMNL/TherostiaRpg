import os
import pickle
import copy

from core.state import character, set_character
from core.Items import load_all_items, UsableItem, Items
from core.load_weapons import load_weapons

SAVE_DIR = "Therostia Saves"

# oad all item and weapon templates from JSON
all_items = load_all_items()
all_weapons = load_weapons()

# rebuild inventory from raw save data
def rebuild_inventory(char):
    rebuilt = {}
    for name, count_or_data in char.inventory.items():
        # Skip if already rebuilt
        if isinstance(count_or_data, dict) and "item" in count_or_data and "count" in count_or_data:
            rebuilt[name] = count_or_data
            continue

        # Rebuild UsableItem
        if name in all_items:
            item_data = all_items[name]
            effect = item_data.get("effect")
            amount = item_data.get("amount", 0)
            item_obj = UsableItem(name, effect, amount)
            rebuilt[name] = {"item": item_obj, "count": count_or_data}
        # Rebuild WeaponTemplate
        elif name in all_weapons:
            item_obj = all_weapons[name]
            rebuilt[name] = {"item": item_obj, "count": count_or_data}
        else:
            print(f"⚠️ Unknown item: {name}")
    char.inventory = rebuilt


# Make sure the save folder exists
def ensure_saves_dir():
    if not os.path.exists(SAVE_DIR):
        os.makedirs(SAVE_DIR)

# List existing files
def list_save_files():
    ensure_saves_dir()
    return [f for f in os.listdir(SAVE_DIR) if f.endswith('.pkl')]

# Create the filename from character data
def format_filename(char):
    safe_name = char.name.strip().replace(" ", "_")
    return f"{safe_name}_Lv{char.level}_HP{char.health}_XP{char.XP}.pkl"

# Prepare inventory for saving (strip out objects)
def prepare_inventory_for_saving(inventory):
    return {name: data["count"] for name, data in inventory.items()}

# Save the character safely
def save_character(char, filename=None):
    ensure_saves_dir()

    safe_name = char.name.strip().replace(" ", "_")

    #if no custom filename, build it
    if not filename:
        filename = format_filename(char)
    path = os.path.join(SAVE_DIR, filename)

    # remove any existing saves for this character
    for f in list_save_files():
        if f.startswith(f"{safe_name}_"):   # matches previous stat-files
            try:
                os.remove(os.path.join(SAVE_DIR, f))
            except OSError:
                pass

    # write the new save
    char_to_save = copy.deepcopy(char)
    char_to_save.inventory = prepare_inventory_for_saving(char_to_save.inventory)
    with open(path, "wb") as f:
        pickle.dump(char_to_save, f)

    print(f"💾 Game saved to {path}")


# Load the character and rebuild inventory
def load_character():
    ensure_saves_dir()
    files = list_save_files()

    if not files:
        print("❌ No save files found.")
        return None

    print("=== SAVES ===")
    for i, f in enumerate(files):
        print(f"{i + 1}) {f}")

    try:
        choice = int(input("Select save number: "))
        if 1 <= choice <= len(files):
            path = os.path.join(SAVE_DIR, files[choice - 1])
            with open(path, "rb") as f:
                loaded_char = pickle.load(f)

            rebuild_inventory(loaded_char)
            set_character(loaded_char)

            print("✅ Save loaded successfully!")
            return loaded_char
        else:
            print("❌ Invalid selection.")
            return None
    except ValueError:
        print("❌ Invalid input.")
        return None
