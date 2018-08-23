import random
import time

choices = {1: "rock", 2: "paper", 3: "scissors"}

welcome_message = """let's play rock paper scissors, you know how to play, let's go!"""


def main():
    print(welcome_message)
    the_game()
    replay()


def the_game():
    while True:
        try:
            print("""\n    Pick Your Poison:
            \n    1 = Rock
    2 = Paper
    3 = Scissors""")
            computer_choice = get_computer_choice()
            player_choice = get_player_choice()
            countdown(3)
            print(str(translate(computer_choice)) + "!")
            if computer_choice == player_choice:
                print("\nit's a tie let's go again!")
                continue
            elif computer_choice == 1 and player_choice == 2:
                print("\nUgh! you beat me with paper, I'll get you next time!")
                break
            elif computer_choice == 1 and player_choice == 3:
                print("\nHa! I beat you with Rock! better luck next time.")
                break
            elif computer_choice == 2 and player_choice == 1:
                print("\nHa! I beat you with paper! Better luck next time.")
                break
            elif computer_choice == 2 and player_choice == 3:
                print("\nUgh! You beat me with scissors! I'll get you next time!")
                break
            elif computer_choice == 3 and player_choice == 1:
                print("\nUgh! you beat me with Rock! I'll get you next time!")
                break
            elif computer_choice == 3 and player_choice == 2:
                print("\nHa! I beat you with scissors! Better luck next time!")
                break
        except ValueError:
            print("\nyou gotta pick something else, try again")
            continue
        else:
            break


def get_computer_choice():
    return random.choice(list(choices.keys()))


def get_player_choice():
    while True:
        try:
            player_choice = int(input("\nPick a choice, choose wisely: "))
        except ValueError:
            print("You gotta pick something different try again")
            continue
        else:
            return player_choice


def countdown(n):
    while n > 0:
        print(n)
        time.sleep(1)
        n = n - 1
        if n == 0:
            break


def translate(i):
    if i == 1:
        return "Rock"
    if i == 2:
        return "Paper"
    if i == 3:
        return "Scissors"


def replay():
    while True:
        try:
            replay_result = input("\nDo you wanna play again? (y/n): ")
            if replay_result == "y":
                the_game()
            elif replay_result == "n":
                print("Till next time!")
                break
        except ValueError:
            print("I didn't quite get that, try again...")
            continue


if __name__ == '__main__':
    main()
