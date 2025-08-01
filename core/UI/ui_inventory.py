from core.load_weapons import WeaponTemplate
from core.state import character

def inventory():
    print("\n📦 === INVENTORY ===")
    if not character.inventory:
        print("Your inventory is empty.")
        return

    weapon_options = []
    index = 1

    print("\n🗡️ Weapons:")
    for item_name, data in character.inventory.items():
        item = data["item"]
        count = data["count"]
        if isinstance(item, WeaponTemplate):
            print(f"  {index}) {item_name} ×{count}  |  +{item.bonus_damage} dmg  ({item.rarity})")
            weapon_options.append(item)
            index += 1

    if not weapon_options:
        print("  You have no weapons.")

    print("\n🧪 Items:")
    for item_name, data in character.inventory.items():
        item = data["item"]
        count = data["count"]
        if not isinstance(item, WeaponTemplate):
            print(f"  - {item_name} ×{count}")

    if weapon_options:
        try:
            choice = int(input("\nChoose a weapon to equip (number): "))
            if 1 <= choice <= len(weapon_options):
                character.weapon = weapon_options[choice - 1]
                print(f"\n✅ You equipped {character.weapon.name}!\n")
            else:
                print("❌ Invalid choice.")
        except ValueError:
            print("❌ Please enter a number.")
