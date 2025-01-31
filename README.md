# Number Guessing Game

## Description

This is a simple number guessing game written in Python. The game randomly selects a number between 1 and 100, and the player has to guess the correct number. After each guess, the game provides hints to guide the player toward the correct number. The game keeps track of all previous guesses and displays them once the player correctly guesses the secret number.

## How to Play

1. Run the script in a Python environment.
2. The game will generate a random number between 1 and 100.
3. The player inputs a guess.
4. The game provides feedback:
   - "Type a smaller number next time" if the guess is too high.
   - "Type a bigger number next time" if the guess is too low.
5. The game continues until the player guesses the correct number.
6. Once the correct number is guessed, the game displays all previous guesses and congratulates the player.

## Prerequisites

- Python 3.x installed on your system

## Running the Game

To play the game, run the following command in your terminal or command prompt:

```sh
python project.py
```
## Notes

- The game prints the secret number at the start for testing purposes. You can use `print(secret_nibe)` for debugging.
- The game does not handle non-integer inputs. Ensure to input valid numbers.



