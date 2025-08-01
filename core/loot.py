from core.Items import UsableItem, Items

def roll_loot(enemy_loot_table):
    import random
    return [item_name for item_name, chance in enemy_loot_table.items() if random.random() < chance]

def resolve_loot_item(item_name, all_weapons, all_items):
    if item_name == "Fist":
        return None
    elif item_name in all_weapons:
        return all_weapons[item_name]
    elif item_name in all_items:
        data = all_items[item_name]
        if "effect" in data:
            return UsableItem(item_name, data["effect"], data["amount"])
        return Items(item_name)
