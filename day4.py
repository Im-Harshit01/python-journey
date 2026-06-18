# Random Number Guessing Game from 1-100

import random

print("Number Guessing Game")
print("I am thinking of a number from 1 to 100.")

secret_number = random.randint(1, 100)
guess = 0

while guess != secret_number:
    guess = int(input("Enter your guess: "))

    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print("Correct! You won!")

