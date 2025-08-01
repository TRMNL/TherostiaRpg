from core.utils import clear_screen, get_colors
from core.UI.ui_character import start_character_creation

CYAN, RESET = get_colors()[3], get_colors()[4]

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
