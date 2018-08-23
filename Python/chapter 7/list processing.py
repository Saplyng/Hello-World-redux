import random

print("Let's play a game, I pick 20 random numbers")
print("And you pick one number 1 to 100, if any of my numbers are")
print("Higher than yours, I win.")
print("If you have the highest number I also win.")


def random_stuff():  # I hate functions
    random_list = random.sample(range(1, 100), 20)

    return random_list


def user_input():  # They're stupid and make an easy solution harder
    while True:
        try:
            user_num = int(input("\nPlease pick a number between 1 and 100: "))
            if not 0 < user_num < 101:
                print("Are you daft? I said between 1 and 100, try again!")
                continue
        except ValueError:
            print("That's not a number try again, stupid Fleshy")
            continue
        else:
            break
    return user_num


refined_list = random_stuff()
refined_input = user_input()
list2 = []


def the_end():  # this one is especially bad, can't even get by without a global
    global list2
    for i in refined_list:
        if i > refined_input:
            list2.append(i)


def condition():
    if len(list2) > 0:
        print("Here are my winning numbers")
        print(list2)
    elif len(list2) == 0:
        print("\nCongratulations, you beat random chance")
        print("I'm sure you're parents would be proud of you")
        print("Either way, I still win")


def main():  # I would have gotten away with it too, if it weren't for you meddling functions
    the_end()
    condition()


if __name__ == '__main__':
    main()
