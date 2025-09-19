import random

def hangman():
    # Predefined list of 5 words
    words = ["python", "apple", "hangman", "orange", "school"]
    word = random.choice(words)  # Randomly choose a word
    guessed = ["_"] * len(word)  # To display correct guesses
    guessed_letters = []  # Store all guessed letters
    attempts = 6  # Wrong guesses allowed

    print("🎯 Welcome to Hangman!")
    print("Word to guess:", " ".join(guessed))

    while attempts > 0 and "_" in guessed:
        guess = input("\nGuess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("❌ Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("⚠️ You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("✅ Good guess!")
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed[i] = guess
        else:
            attempts -= 1
            print(f"❌ Wrong! Attempts left: {attempts}")

        print("Word:", " ".join(guessed))
        print("Guessed letters:", ", ".join(guessed_letters))

    if "_" not in guessed:
        print("\n🎉 Congratulations! You guessed the word:", word)
    else:
        print("\n💀 Game over! The word was:", word)

# Run the game
hangman()