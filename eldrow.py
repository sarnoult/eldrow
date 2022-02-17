import argparse

from colorama import init, Style, Back
from urllib.request import urlopen
from random import choice

init()

VOCAB_URL = "https://raw.githubusercontent.com/jason-chao/wordle-solver/main/english_words_original_wordle.txt"
VOCABULARY = [line.strip() for line in urlopen(VOCAB_URL)]


def pick_word():
    word = choice(VOCABULARY).decode("utf-8")
    print("Let's play wordle!")
    print(f"Correct word (for testing): {word}")
    return word


def read_guess(attempt_nb):
    print(f"Enter your next guess:")
    while True:
        guess = input(f"[{attempt_nb}] ")
        if len(guess) != 5:
            print("Please enter a 5-letter word")
        elif guess.encode("utf-8") not in VOCABULARY:
            print("Unknown word, try again")
        else:
            break
    return guess


def check(guess, word):
    output = []
    for i in range(5):
        if guess[i] == word[i]:
            output.append(Back.GREEN)
        elif guess[i] in word:
            output.append(Back.YELLOW)
        output.append(guess[i])
        output.append(Style.RESET_ALL)
    return output


def play(max_nb_attempts):
    word = pick_word()
    found_solution = False
    for attempt in range(1, max_nb_attempts + 1):
        guess = read_guess(attempt)
        output = check(guess, word)
        print("".join(output))
        if word == guess:
            print(f"Congrats! You needed {attempt} attempts")
            found_solution = True
    if not found_solution:
        print(f"Bad luck! We were looking for {word}")


if __name__ == '__main__':
    # parser = argparse.ArgumentParser(description=__doc__)
    # parser.add_argument("max_nb_attempts", type=int, help="Maximum number of attempts")
    # parser.add_argument("word_length", type=int, help="Word length")
    # args = parser.parse_args()
    play(6)
