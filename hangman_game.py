# Project : Hangman Game in python
# Instructor : Kinza Shakil
# Quarter 3 GIAIC

import random
words = ['enum', 'python', 'collab', 'vscode', 'game']

word = random.choice(words)
guessed_letters = []
attempts = 6

print("Welcome to Hangman Game Project")
print("_" * len(word))

while attempts > 0:  # Add colon here
    guess = input("\nGuess the letters: ").lower()
    
    if len(guess) != 1 or not guess.isalpha():
        print("Please write one alphabet only!")
        continue
    if guess in guessed_letters:
        print("This letter has already been guessed. Choose another letter.")
        continue
    guessed_letters.append(guess)

    if guess in word:
        print("Correct guess!")
    else:
        attempts -= 1
        print(f"Wrong guess! {attempts} attempts remaining.")

    displayed_word = " ".join([letter if letter in guessed_letters else "_" for letter in word])
    print(displayed_word)

    if "_" not in displayed_word:
        print(f"Congratulations! The correct word is: {word}")
        break
else:
    print(f"Game Over! The correct word was: {word}")
