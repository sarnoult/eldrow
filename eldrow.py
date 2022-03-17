import argparse
from typing import List

from colorama import init, Style, Back
from urllib.request import urlopen
from random import choice

init()

VOCAB_URL = "https://raw.githubusercontent.com/jason-chao/wordle-solver/main/english_words_original_wordle.txt"
VOCABULARY = [line.strip() for line in urlopen(VOCAB_URL)]

WORD_LENGTH = 5


def pick_word() -> str:
    """Selects a word from the vocabulary"""
    word = choice(VOCABULARY).decode("utf-8")
    print("Let's play wordle!")
    print(f"Correct word (for testing): {word}")
    return word


def read_guess(attempt_nb: int) -> str:
    """Prompts the user for a guess"""
    print(f"Enter your next guess:")
    while True:
        guess = input(f"[{attempt_nb}] ")
        if len(guess) != WORD_LENGTH:
            print("Please enter a 5-letter word")
        elif guess.encode("utf-8") not in VOCABULARY:
            print("Unknown word, try again")
        else:
            break
    return guess


def color_correct(char: str) -> List[str]:
    return "".join([Back.GREEN, char, Style.RESET_ALL])


def color_inword(char: str) -> List[str]:
    return "".join([Back.YELLOW, char, Style.RESET_ALL])


def validate_char(i: int, guess: str, solution: str) -> str:
    if guess[i] == solution[i]:
        return color_correct(guess[i])
    elif guess[i] in solution:
        return color_inword(guess[i])
    else:
        return guess[i]


def validate(guess: str, solution: str) -> str:
    """Validates the user guess against the solution, coloring correct characters"""
    return "".join([validate_char(i, guess, solution) for i in range(WORD_LENGTH)])


def play(max_nb_attempts: int):
    """Plays wordle until user finds solution or number of attempts is exceeded"""
    word = pick_word()
    found_solution = False
    for attempt in range(1, max_nb_attempts + 1):
        guess = read_guess(attempt)
        output = validate(guess, word)
        print(output)
        if word == guess:
            print(f"Congrats! You needed {attempt} attempts")
            found_solution = True
    if not found_solution:
        print(f"Bad luck! We were looking for {word}")


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("max_nb_attempts", type=int, default=10, help="Maximum number of attempts")
    args = parser.parse_args()
    play(args.max_nb_attempts)
