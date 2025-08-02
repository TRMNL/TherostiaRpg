# core/state.py
from core.character import CharacterTemplate
from core.load_weapons import load_weapons
from core.Items       import load_all_items

all_weapons   = load_weapons()
all_items     = load_all_items()
last_looted_items = []

character = CharacterTemplate(
    name="", level=1,
    health=100, MaxHP=100,
    damage=2, XP=0, MaxXP=100,
    minMana=10, maxMana=10,
    weapon=None, inventory={}
)

def set_character(new_char):
    # Copy over all the attributes
    for attr in (
        "name","level","health","MaxHP",
        "damage","XP","MaxXP",
        "minMana","maxMana","weapon"
    ):
        setattr(character, attr, getattr(new_char, attr))

    # Replace inventory contents in-place
    character.inventory.clear()
    character.inventory.update(new_char.inventory)

    # Clear/refill the recent‐loot list
    last_looted_items.clear()
    last_looted_items.extend(new_char.inventory.keys())
