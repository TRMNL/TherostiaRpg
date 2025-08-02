
import json

class Items:
    def __init__(self, name):
        self.name = name

class UsableItem(Items):
    def __init__(self, name, effect, amount):
        super().__init__(name)
        self.effect = effect
        self.amount = amount

    def use(self, character): 
        if self.effect == "heal":
            character.health = min(character.health + self.amount, character.MaxHP)
            print(f"{character.name} heals for {self.amount} HP.")
            
def load_all_items():
    all_items = {}
    item_types = ["potions", "crafting", "currency", "junk", "food"]
    for item_type in item_types:
        with open(f"Jsons\items\{item_type}.json", "r") as f:
            data = json.load(f)
            for name, props in data.items():
                props["type"] = item_type
                all_items[name] = props
    return all_items


def use_healing_potion(character):
    for item_name, data in character.inventory.items():
        item = data["item"]
        if isinstance(item, UsableItem) and item.effect == "heal":
            item.use(character)
            data["count"] -= 1
            if data["count"] <= 0:
                del character.inventory[item_name]
            return
    print("❌ No Healing Potion!")
