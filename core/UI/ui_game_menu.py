import os
import time
from core.state import character
from core.UI.ui_inventory import inventory
from core.utils import get_colors

GREEN = get_colors()[1]

def game_menu():
    while character.health > 0:
        os.system("cls" if os.name == "nt" else "clear")
        print(f"{GREEN}==== Adventure Menu ====\033[0m")
        print("1) Attack")
        print("2) Boss Room (Coming Soon)")
        print("3) Inventory")
        choice = input("What will you do? ")

        if choice == "1":
            from core.game import gameloop  # Imported here to avoid circular dependency
            gameloop()
        elif choice == "2":
            print("👹 Boss Room is under construction...")
            input("Press Enter to return...")
        elif choice == "3":
            inventory()
            input("Press Enter to return...")
        else:
            print("Invalid choice.")
            time.sleep(1)
