from game import Game

def get_user_menu_choice():
    print("Menu:")
    print("1. Play a new game")
    print("2. Show scores")
    print("3. Quit")

    choice = input("Please select an option (1/2/3): ").strip()
    while choice not in ["1", "2", "3"]:
        print("Invalid choice. Please select 1, 2, or 3.")
        choice = input("Please select an option (1/2/3): ").strip()

    return choice

def print_results(results):
    print("Game Results:")
    for key, value in results.items():
        print(f"{key.capitalize()}: {value}")
    print("Thank you for playing!")

def main():
    game = Game()
    results = {"win": 0, "loss": 0, "draw": 0}

    while True:
        choice = get_user_menu_choice()

        if choice == "1":
            result = game.play()
            results[result] += 1
        elif choice == "2":
            print_results(results)
        else:
            print_results(results)
            break

if __name__ == "__main__":
    main()
