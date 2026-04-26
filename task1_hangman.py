"""
CodeAlpha Internship - Task 1: Hangman Game
Author: CodeAlpha Intern
Description: A text-based Hangman game where the player guesses a word one letter at a time.
"""

import random

# Predefined list of words
WORDS = ["python", "developer", "hangman", "keyboard", "monitor"]

# Hangman visual stages (0 = full, 6 = empty)
HANGMAN_STAGES = [
    """
   -----
   |   |
   O   |\
   |
  /|\\  |
  / \\  |
       |
=========
""",
    """
   -----
   |   |
   O   |
  /|\\  |
  /    |
       |
=========
""",
    """
   -----
   |   |
   O   |
  /|\\  |
       |
       |
=========
""",
    """
   -----
   |   |
   O   |
  /|   |
       |
       |
=========
""",
    """
   -----
   |   |
   O   |
   |   |
       |
       |
=========
""",
    """
   -----
   |   |
   O   |
       |
       |
       |
=========
""",
    """
   -----
   |   |
       |
       |
       |
       |
=========
""",
]


def display_status(word, guessed_letters, wrong_guesses):
    """Display the current game status."""
    print(HANGMAN_STAGES[6 - wrong_guesses])

    # Show the word with blanks
    display_word = " ".join(
        letter if letter in guessed_letters else "_" for letter in word
    )
    print(f"  Word: {display_word}")
    print(f"  Wrong guesses left: {6 - wrong_guesses}")

    if guessed_letters:
        wrong = [l for l in guessed_letters if l not in word]
        if wrong:
            print(f"  Incorrect letters: {', '.join(sorted(wrong))}")
    print()


def hangman():
    """Main Hangman game function."""
    print("=" * 40)
    print("       WELCOME TO HANGMAN GAME!")
    print("=" * 40)

    word = random.choice(WORDS)
    guessed_letters = set()
    wrong_guesses = 0
    max_wrong = 6

    while wrong_guesses < max_wrong:
        display_status(word, guessed_letters, wrong_guesses)

        # Check win condition
        if all(letter in guessed_letters for letter in word):
            print(f"🎉 Congratulations! You guessed the word: '{word.upper()}'")
            break

        # Get player input
        guess = input("  Enter a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("  ⚠  Please enter a single valid letter.\n")
            continue

        if guess in guessed_letters:
            print(f"  ⚠  You already guessed '{guess}'. Try another letter.\n")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"  ✅ Good guess! '{guess}' is in the word.\n")
        else:
            wrong_guesses += 1
            remaining = max_wrong - wrong_guesses
            print(f"  ❌ Wrong! '{guess}' is not in the word. {remaining} guesses left.\n")

    else:
        display_status(word, guessed_letters, wrong_guesses)
        print(f"💀 Game Over! The word was: '{word.upper()}'")

    print("\nThanks for playing Hangman!")


if __name__ == "__main__":
    hangman()
