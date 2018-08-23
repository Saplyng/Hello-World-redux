initial_dialog = """Hello User, it's that time of month again!
Yep it's time to pay your phone bill! So much fun, well at least for me.

I do love getting your money, User... (´｡• ω •｡`)

But before I can get all your precious money, I need to know what package you have.
In case you forgot your packages name, I put all of them in a pretty list for you.

Aren't I nice? 	\(^ヮ^)/

Just type in the number (shown left) that corresponds to your package.
"""

# gotta be snarky whenever possible, I love my computers snarky and sarcastic
print(initial_dialog)

# this is for later, to make sure that user input gets evaluated properly
a, b, c = [1, 2, 3]

phone_packages = ["Package A: For $39.99 per month 450 minutes are provided. Additional minutes are $0.45 per minute.",
                  "Package B: For $59.99 per month 900 minutes are provided. Additional minutes are $0.40 per minute.",
                  "Package C: For $69.99 per month unlimited minutes provided."]

# for the user
for item in enumerate(phone_packages, 1):
    print("[%d] %s" % item)

# prevents user from breaking program, no errors should appear. reappears later.
# again, to make sure tha user input doesnt break the program
while True:
    try:
        user_package = int(input("\nPlease select your package\'s number: "))
        # this was actually pretty hard to do, but with this the user
        # can't do anything but 1, 2, or 3 which all correspond to the phone packages
        if not (user_package == int(a) or user_package == int(b) or user_package == int(c)):
            print("You fail at typing numbers, try again")
            continue
    except ValueError:
        print("You have to type a number not a letter. Did you even read?")
        continue
    else:
        break

# all the nested ifs are here, along with loops in ifs
if user_package == a:
    while True:
        try:
            user_minutes = int(input("How many total minutes did you use?: "))
            if user_minutes < 0:
                print("You\'re just trying to be \"smart\" aren\'t you?")
                continue
        except ValueError:
            print("You have to type a number not a letter. Did you even read?")
            continue
        else:
            break
    if user_minutes > 450:
        user_overage = user_minutes - 450
        user_debt = 0.45 * user_overage + 39.99
        print("Your fee this month will be " + '$' + format(user_debt, '.2f'))
    elif user_minutes <= 450:
        print("Your fee for this month will be $39.99")
elif user_package == b:
    while True:
        try:
            user_minutes = int(input("How many total minutes did you use?: "))
            if user_minutes < 0:
                print("You\'re just trying to be \"smart\" aren\'t you?")
                continue
        except ValueError:
            print("You have to type a number not a letter. Did you even read?")
            continue
        else:
            break
    if user_minutes > 900:
        user_overage = user_minutes - 900
        user_debt = 0.40 * user_overage + 59.99
        print("Your fee for this month will be " + "$" + format(user_debt, '.2f'))
    elif user_minutes <= 900:
        print("Your fee for this month will be $59.99")
elif user_package == c:
    print("Somebody\'s got more minutes than they could ever use!")
    print("Your fee for this month will be $69.99")
else:
    print("This statement should never appear if i\'ve done everything right...")

print("\nI expect the money by Monday, User.")
print("Thanks for your business! 	(*¯︶¯*)")
input("\nHIT ENTER TO END")
