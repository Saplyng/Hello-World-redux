with open('BoyNames.txt', 'r') as f:
    boy_names = [line.strip() for line in f]


with open('GirlNames.txt', 'r') as g:
    girl_names = [line.strip() for line in g]


initial_dialog = """
Hello User!
I don't really care what your name is, but I bet you do!

So why don't we find out if your name is super popular, or
to put it another way ridiculously common and unoriginal!

Let's find out together! :D"""

print(initial_dialog)


while True:
    try:
        user_name = str(input("\nWhat's your name, User?: ").lower).rstrip
        if user_name is int:
            print("Your name isn't a number, and if it is, then type it out.")
            continue
    except ValueError:
        print("Don't know why this showed up, but assume you did something wrong.")
    else:
        break


if user_name in girl_names:
    print("Hey! your name is popular, Congratulations...")
elif user_name in boy_names:
    print("Hey! your name is popular, Congratulations...")
else:
    print("Oooh, a non-popular name, that's interesting.")
