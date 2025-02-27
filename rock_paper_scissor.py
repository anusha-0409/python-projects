import random

choices = ["rock", "paper", "scissors"]

def get_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        return "You win!"
    else:
        return "You lose!"

def play():
    user_choice = input("Enter rock, paper, or scissors: ").lower()
    if user_choice not in choices:
        print("Invalid choice. Try again.")
        return

    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    result = get_winner(user_choice, computer_choice)
    print(result)

play()
#the commit check