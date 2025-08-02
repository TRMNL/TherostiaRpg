import time
from core.enemy_loader import spawn_enemy
from core.loot import roll_loot, resolve_loot_item
from core.level_up import level_up
from core.UI.ui_overlay import show_ui
from core.UI.ui_inventory import inventory
from core.state import character, last_looted_items, all_weapons, all_items
from core.Items import use_healing_potion
from core.save_system import save_character

def gameloop():
    while character.health > 0:
        enemy, loot_table, xp_reward = spawn_enemy(character)
        print(f"\n⚔️ A wild {enemy.name} appears!")

        while character.health > 0 and enemy.health > 0:
            show_ui(enemy)
            choice = input("Choose your action: ")

            match choice:
                case "1":
                    character.attack(enemy)
                    if enemy.health > 0:
                        enemy.attack(character)
                case "2":
                    use_healing_potion(character)
                case "3":
                    inventory()
                case "4":
                    
                    return
                case _:
                    print("Invalid choice.")
                    time.sleep(1)

        if character.health <= 0:
            print(f"\n💀 {character.name} has been defeated...")
            break

        print(f"\n✅ The {enemy.name} has been slain! Victory is yours!")
        print(f"🎯 You gained {xp_reward} XP!")
        character.XP += xp_reward
        level_up(character)

        loot = roll_loot(loot_table)
        last_looted_items.clear()

        if loot:
            for item_name in loot:
                item = resolve_loot_item(item_name, all_weapons, all_items)
                if item:
                    if item_name in character.inventory:
                        character.inventory[item_name]["count"] += 1
                    else:
                        character.inventory[item_name] = {"item": item, "count": 1}
                    last_looted_items.append(item_name)