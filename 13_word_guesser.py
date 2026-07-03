# Word guessing game (Hangman) implementation in Python.



import random

def play_hangman():
    word_bank = ["python", "computer", "program", "exception", "variable", "condition", "glyph", "sphynx", "phlegm", "rythm", "myst", "schism", "lynx",
                 "crypt", "jazz", "buzz", "fizz", "puzzle", "quizzical", "whiskey", "xylophone", "zephyr"]
    secret_word = random.choice(word_bank)
    
    guessed_letters = set()
    max_turns = 6
    turns_left = max_turns

    print("Welcome to Hangman!")
    print("Try to guess the secret word letter by letter.")

    # 2. Main Game Loop
    while turns_left > 0:
        display_word = []
        for letter in secret_word:
            if letter in guessed_letters:
                display_word.append(letter)
            else:
                display_word.append("_")
        
        current_progress = " ".join(display_word)
        print(f"\nWord: {current_progress}")
        print(f"Turns left: {turns_left}")
        
        # Check if the player won
        if "_" not in display_word:
            print(f"🎉 Congratulations! You guessed the word: {secret_word}")
            break

        # 3. Get and validate user input
        guess = input("Guess a letter: ").lower().strip()

        # Exception/Validation handling for inputs
        if len(guess) != 1 or not guess.isalpha():
            print("❌ Invalid input. Please enter a single alphabetical letter.")
            continue
        
        if guess in guessed_letters:
            print(f"⚠️ You already guessed '{guess}'. Try a different letter.")
            continue

        # 4. Process the guess
        guessed_letters.add(guess)

        if guess in secret_word:
            print(f"✅ Good job! '{guess}' is in the word.")
        else:
            print(f"❌ Oops! '{guess}' is not in the word.")
            turns_left -= 1

    # 5. Game Over check
    if turns_left == 0:
        print(f"\n💀 Game over! You ran out of turns. The word was: {secret_word}")



if __name__ == "__main__":
    play_hangman()