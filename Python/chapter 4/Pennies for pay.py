initial_dialog = """ Hello User, today it's story time.

There was once an impoverished boy who tricked a king into giving him enough food
to feed himself for a lifetime...

How did he do this?

Well he asked the king to give him a grain of rice and that he double the amount
for every square on a chess board.

Today we'll do something similar, except instead of rice we'll be using money!

So User, just type in how many days you'd like to be paid,
and i'll tell you how much you made...
"""

print(initial_dialog)


while True:
    try:
        user_days = int(input("How many days would you like to be paid for? "))
        if not user_days > 0:
            print("We can't pay you for zero days or less,")
            print("You're getting money here, just type in a real number")
            continue
    except ValueError:
        print("that's not a number, give me a NUMBER of days")
        continue
    else:
        break

payday = 0.01
total = 0

for day in range(1, user_days + 1):
    print(("Day: " + str(day) + "   " + format(payday, ",.2f")))
    if day <= user_days:
        total += payday
        payday = payday * 2


print("You earned a total of $" + format(total, ",.2f"))

print("\nTry not to spend it all in one place!")
