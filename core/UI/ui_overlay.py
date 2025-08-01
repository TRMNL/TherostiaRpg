from core.utils import get_colors
from core.state import character, last_looted_items
from core.load_weapons import WeaponTemplate
from core.UI.ui_inventory import inventory
from core.UI.ui_game_menu import game_menu

RED, GREEN, YELLOW, CYAN, RESET = get_colors()

def hp_bar(current, max_hp, bar_length=20):
    filled_length = int(bar_length * current // max_hp)
    bar = "█" * filled_length + "░" * (bar_length - filled_length)
    return f"[{bar}] {current}/{max_hp}"

def xp_bar(current, max_xp, bar_length=20):
    filled_length = int(bar_length * current // max_xp)
    bar = "█" * filled_length + "░" * (bar_length - filled_length)
    return f"[{bar}] {current}/{max_xp}"

def show_ui(enemy):
    print("\033[H\033[J", end="")
    print(f"{YELLOW} Therostia {RESET}")
    print("=" * 40)
    print(f"{CYAN}🧍 {character.name} [Lv {character.level}]{RESET}")
    print(f"{GREEN}❤️ HP: {hp_bar(character.health, character.MaxHP)}{RESET}")
    print(f"✨ XP: {xp_bar(character.XP, character.MaxXP)}")
    print(f"🗡️ Weapon: {character.weapon.name if character.weapon else 'None'} | Damage: {character.damage + (character.weapon.bonus_damage if character.weapon else 0)}")
    print("-" * 40)
    print(f"{RED}👾 {enemy.name}{RESET}")
    print(f"{RED}❤️ HP: {hp_bar(enemy.health, enemy.MaxHP)}{RESET}")
    print("=" * 40)
    print("🎮 Choose your action:")
    print("1️⃣  Attack")
    print("2️⃣  Use Healing Potion")
    print("3️⃣  Open Inventory")
    print("4️⃣  Back out")
    if last_looted_items:
        print(f"\n📦 Looted Items: {', '.join(last_looted_items)}")
