import random

class Game:
    def get_user_item(self):
        user_item = input("Please select an item (rock/paper/scissors): ").lower()
        while user_item not in ["rock", "paper", "scissors"]:
            print("Invalid input. Please select rock, paper, or scissors.")
            user_item = input("Please select an item (rock/paper/scissors): ").lower()
        return user_item

    def get_computer_item(self):
        return random.choice(["rock", "paper", "scissors"])

    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            return "draw"
        elif (user_item == "rock" and computer_item == "scissors") or \
             (user_item == "paper" and computer_item == "rock") or \
             (user_item == "scissors" and computer_item == "paper"):
            return "win"
        else:
            return "loss"

    def play(self):
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(user_item, computer_item)

        print(f"You selected {user_item}. The computer selected {computer_item}.")

        if result == "win":
            print("You win!")
        elif result == "draw":
            print("It's a draw!")
        else:
            print("You lose!")

        return result

