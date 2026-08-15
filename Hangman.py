
import random

words = ["python", "apple", "computer", "coding", "internship"]

secret_word = random.choice(words)

display_word = ["_"] * len(secret_word)

incorrect_guesses = 0
max_guesses = 6

guessed_letters = []

print("Welcome to Hangman!")
print("Guess the secret word.")
print(" ".join(display_word))


while incorrect_guesses < max_guesses and "_" in display_word:

    guess = input("\nEnter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("Correct guess!")

        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display_word[i] = guess

    else:
        incorrect_guesses += 1
        print("Wrong guess!")
        print("Incorrect guesses:", incorrect_guesses, "/", max_guesses)

    print("Word:", " ".join(display_word))

if "_" not in display_word:
    print("\nCongratulations! You guessed the word!")
    print("The word was:", secret_word)
else:
    print("\nGame Over!")
    print("The correct word was:", secret_word)
