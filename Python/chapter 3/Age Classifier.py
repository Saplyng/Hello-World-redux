initial_msg = """
Hello User! today we have to ask you an awkward question.

I know what you're thinking, "oh no, what horrible thing will this computer
ask me?"

well ponder no further User, because the horrible question I bestow upon you is this...
"""

print(initial_msg)

while True:
    try:
        user_age = int(input("What is your age? "))
    except ValueError:
        print("C\'mon, no dodging the question!")
    else:
        break


infant = 0 <= user_age <= 1
child = 1 < user_age <= 13
teenager = 13 < user_age <= 20
adult = 20 < user_age <= 120

print(" ")

if infant:
    print("you're just an infant... how\'d you even read this?")
elif child:
    print("Oh, so you're a child, congratulations on making it this far.")
elif teenager:
    print("So, you're a young adult, gotten a taste of the world yet?")
elif adult:
    print("Oh, you\'re an adult, I\'m so sorry. but you still have plenty")
    print("of time to get over how old that makes you feel.")
else:
    print("Just face the truth, are you even human?")
