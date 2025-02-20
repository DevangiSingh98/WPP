import random

class RockPaperScissors:
    def __init__(self, rounds):
        self.rounds = rounds
        self.currentround = 0
        self.userwins = 0
        self.computerwins = 0

    def get_computer_choice(self):
        return random.choice(["rock", "paper", "scissors"])

    def play_game(self):
        print("Let's play Rock-Paper-Scissors.")

        while self.currentround < self.rounds:
            self.currentround += 1
            print(f"\nRound {self.currentround}")

            userchoice = input("Choose rock, paper, or scissors: ").lower()
            while userchoice not in ["rock", "paper", "scissors"]:
                print("Invalid choice, try again!")
                userchoice = input("Choose rock, paper, or scissors: ").lower()

            computerchoice = self.get_computer_choice()
            print(f"Computer chose: {computerchoice}")

            if userchoice == computerchoice:
                print("It's a tie!")
            elif (userchoice == "rock" and computerchoice == "scissors") or \
                 (userchoice == "paper" and computerchoice == "rock") or \
                 (userchoice == "scissors" and computerchoice == "paper"):
                print("You win this round.")
                self.userwins += 1
            else:
                print("Computer wins this round.")
                self.computerwins += 1

        print("\nGame Over!")
        print(f"Final Score - You: {self.userwins}, Computer: {self.computerwins}")

        if self.userwins > self.computerwins:
            print("You win the game.")
        elif self.userwins < self.computerwins:
            print("Computer wins the game.")
        else:
            print("It's a tie!")

rounds = int(input("Enter number of rounds to play: "))
game = RockPaperScissors(rounds)
game.play_game()
