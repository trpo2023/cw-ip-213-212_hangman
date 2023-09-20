# Path fix
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.dirname(current_dir)
sys.path.append(project_dir)
# end path fix

from src.libhangman.hangman import HangmanGame
import random
import pytest

def test_start_game():
    word_list = ["apple", "banana", "cherry", "grape", "orange"]
    game = HangmanGame(word_list, max_guesses=6)
    game.start_game()

    assert game.in_progress is True
    assert game.guesses_left == 6
    assert game.secret_word in word_list

def test_make_correct_guess():
    word_list = ["apple", "banana", "cherry", "grape", "orange"]
    game = HangmanGame(word_list, max_guesses=6)
    game.is_debug = True
    game.start_game()
    game.secret_word = "banana"
    game.make_guess("b")

    assert game.guesses_left == 6
    assert "b" in game.guesses
    assert game.display_word() == "b_____"

def test_make_correct_guess2():
    word_list = ["apple"]
    game = HangmanGame(word_list, max_guesses=6)
    game.is_debug = True
    game.start_game()
    game.make_guess("b")

    assert game.guesses_left == 5
    assert "b" in game.guesses
    assert game.display_word() == "_____"

def test_make_correct_guess3():
    word_list = ["apple"]
    game = HangmanGame(word_list, max_guesses=6)
    game.is_debug = True
    game.start_game()
    game.make_guess("p")
    game.make_guess("e")

    assert game.guesses_left == 6
    assert "p" in game.guesses
    assert game.display_word() == "_pp_e"

if __name__ == "__main__":
    pytest.main()
