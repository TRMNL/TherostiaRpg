# core/loaders/load_weapons.py

class WeaponTemplate:
    def __init__(self, name, bonus_damage, element, rarity):
        self.name = name
        self.bonus_damage = bonus_damage
        self.element = element
        self.rarity = rarity

import json

def load_weapons(filepath="weapons\weapons.json"):
    with open(filepath, "r") as f:
        data = json.load(f)
    return {name: WeaponTemplate(name, **props) for name, props in data.items()}

# Example usage:
# weapons = load_weapons()
