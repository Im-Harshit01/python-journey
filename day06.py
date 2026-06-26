#This is a simple Rock Paper Scissors game which uses loop condition

import random

print("Rock, Paper, Scissors Game")
options = ["ROCK", "PAPER", "SCISSORS"]

while True:
    print("\n---NEW ROUND---")
    print("Choose your options\n")
    computer_choice = random.choice(options)
    
    guess = input("Rock, Paper, or Scissors (X to exit): ").strip().upper()
    
    if guess == "X":
        print("Thanks for playing!")
        break
        
    if guess not in options:
        print("Invalid choice. Please try again.")
        continue 

    print(f"\nYour Choice: {guess}")
    print(f"Computer's Choice: {computer_choice}\n")
    
    if guess == computer_choice:
        print("It's a tie!")
    elif (guess == "ROCK" and computer_choice == "SCISSORS") or \
         (guess == "PAPER" and computer_choice == "ROCK") or \
         (guess == "SCISSORS" and computer_choice == "PAPER"):
        print("You win!")
    else:
        print("You lose!")