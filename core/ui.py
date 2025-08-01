import os
import time
from core.utils import clear_screen, get_colors
from core.Items import UsableItem, load_all_items
from core.load_weapons import load_weapons, WeaponTemplate
from core.state import character, all_weapons, all_items
from core.game import gameloop

# Unpack color constants
RED, GREEN, YELLOW, CYAN, RESET = get_colors()

def hp_bar(current, max_hp, bar_length=20):
    filled_length = int(bar_length * current // max_hp)
    bar = "█" * filled_length + "░" * (bar_length - filled_length)
    return f"[{bar}] {current}/{max_hp}"

def xp_bar(current, max_xp, bar_length=20):
    filled_length = int(bar_length * current // max_xp)
    bar = "█" * filled_length + "░" * (bar_length - filled_length)
    return f"[{bar}] {current}/{max_xp}"

def show_main_menu():
    while True:
        clear_screen()
        print(f"{CYAN}==== Welcome to Therostia ===={RESET}")
        print("1) New Game")
        print("2) Load Game (Coming Soon)")
        print("3) Quit")
        choice = input("Choose an option: ")
        if choice == "1":
            return start_character_creation()
        elif choice == "2":
            print("🔒 Load Game is not implemented yet.")
            input("Press Enter to continue...")
        elif choice == "3":
            exit()
        else:
            print("❌ Invalid choice. Try again.")

def start_character_creation():
    os.system("cls" if os.name == "nt" else "clear")
    print(f"{YELLOW}--- Character Creation ---{RESET}")
    name = input("Enter your character's name: ")

    all_weapons.clear()
    all_weapons.update(load_weapons())
    all_items.clear()
    all_items.update(load_all_items())

    character.name = name
    character.level = 1
    character.health = 100
    character.MaxHP = 100
    character.XP = 0
    character.MaxXP = 100
    character.damage = 2
    character.weapon = all_weapons["Fist"]
    character.inventory.clear()
    character.inventory["Fist"] = {"item": character.weapon, "count": 1}
    character.inventory["Wooden Sword"] = {"item": all_weapons["Wooden Sword"], "count": 1}

    healing_data = all_items["Healing Potion"]
    potion = UsableItem("Healing Potion", healing_data["effect"], healing_data["amount"])
    character.inventory[potion.name] = {"item": potion, "count": 2}
