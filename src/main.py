import os
import sys
from libhangman.hangman import HangmanGame

def show_menu():
    print("\nИгра Виселица")
    print("1. Начать новую игру")
    print("2. Сделать предположение")
    print("3. Выйти")

def clear_console():
    if sys.platform.startswith('win'):
        os.system('cls')
    else:
        print('\033c', end='')

def main():
    word_list = ["яблоко", "банан", "вишня", "виноград", "апельсин"]
    max_guesses = 6

    game = HangmanGame(word_list, max_guesses)

    while True:
        if game.in_progress:
            game.display_word()
            print("\nПопыток: " + str(game.guesses_left) + "/" + str(max_guesses))

        show_menu()
        choice = input("Выберите нужное действие (1/2/3): ")

        if choice == "1":
            game.start_game()
            clear_console()
        elif choice == "2":
            if game.in_progress:
                letter = input("Введите букву: ").lower()
                game.make_guess(letter)
                clear_console()
            else:
                print("Игра не начата. Начните новую игру сначала.")
        elif choice == "3":
            print("До свидания!")
            break
        else:
            print("Неверный выбор. Введите 1, 2 или 3.")

if __name__ == "__main__":
    main()


if __name__ == "__main__":
    main()
