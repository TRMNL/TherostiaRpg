import os
from core.utils import get_colors
from core.Items import UsableItem, load_all_items
from core.load_weapons import load_weapons, WeaponTemplate
from core.state import character, all_weapons, all_items

YELLOW, RESET = get_colors()[2], get_colors()[4]

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
    