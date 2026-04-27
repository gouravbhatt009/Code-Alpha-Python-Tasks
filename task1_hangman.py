"""
Project Name: Hangman Game
Author: [Your Name]
Course: BCA Final Year
Description: A classic word-guessing game built with Python.
"""

import random

# List of words for the game
# In a real project, you could also load these from a text file
words = ["python", "programming", "database", "network", "software", "security"]

# Visual representation of the hangman
# Organized from 0 errors to 6 errors
stages = [
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / 
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |    
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |    
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |    |
       |    
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |    
       |    
       |
    ---------
    """,
    """
       ------
       |    |
       |    
       |    
       |    
       |
    ---------
    """
]

def play_hangman():
    # 1. Initialize Game State
    chosen_word = random.choice(words).lower()
    guessed_letters = []
    attempts_left = 6
    
    print("--- Welcome to the Hangman Game! ---")
    
    # 2. Main Game Loop
    while attempts_left > 0:
        # Display the current status of the word
        # Using a simple loop to build the display string
        display_word = ""
        for char in chosen_word:
            if char in guessed_letters:
                display_word += char + " "
            else:
                display_word += "_ "
        
        print(stages[attempts_left])
        print(f"Word: {display_word}")
        print(f"Attempts remaining: {attempts_left}")
        print(f"Guessed so far: {', '.join(guessed_letters)}")
        
        # 3. Check if player has won
        if "_" not in display_word:
            print("\nCongratulations! You saved the man and guessed the word!")
            break
            
        # 4. Get User Input
        guess = input("\nEnter a letter: ").lower()
        
        # Validation
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
            
        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try again.")
            continue
            
        # 5. Process the Guess
        guessed_letters.append(guess)
        
        if guess in chosen_word:
            print(f"Good job! '{guess}' is in the word.")
        else:
            attempts_left -= 1
            print(f"Sorry, '{guess}' is not there.")
            
    # 6. End of Game
    if attempts_left == 0:
        print(stages[0])
        print(f"Game Over! The man was hanged. The word was: {chosen_word}")

if __name__ == "__main__":
    play_hangman()
