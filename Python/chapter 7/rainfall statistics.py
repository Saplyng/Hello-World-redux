initial_dialog = ("""Hello User, you must be an aspiring meteorologist!
that's the only reason I can think you would want something like
an rainfall statistics calculator.

But what would I know, I'm just a robot

Anyway, I wont burden you the hassle of converting your units, just be
consistent, if you start with Inches you better not change to Centimeters
by the end.

But since your too lazy to do some simple math yourself, I'm sure I won't
have to worry about that...

But what would I know, I'm just a robot\n""")

print(initial_dialog)


months = ('January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December')
rainfall_num = []

print("just type in the rainfall for each month,")
print("I'll do the rest of the work\n")

for i in months:
    while True:
        try:
            rainfall_num.append(float(input(i + ": ")))
            if not rainfall_num[-1] >= 0:
                del rainfall_num[-1]
                print("I don't think your number was quite right, try again")
                continue
        except ValueError:
            print("You have to type something different that")
            continue
        else:
            break

total_rainfall = sum(rainfall_num)
average_rainfall = total_rainfall / 12


def finding_max():
    for k, j in enumerate(rainfall_num):
        if j == max(rainfall_num):
            return k


def finding_min():
    for k, j in enumerate(rainfall_num):
        if j == min(rainfall_num):
            return k


print("\nTotal Rainfall: " + str(format(total_rainfall, ",.2f")) + " units")
print("Average Rainfall per month over a year: " +
      str(format(average_rainfall, ',.2f') + " units"))


print("\nThe month with the most rain was " +
      str(months[finding_max()]) + " with: " +
      str(format(rainfall_num[finding_max()], ",.2f")) + " units")

print("The month with the least rain was " +
      str(months[finding_min()]) + " with: " +
      str(format(rainfall_num[finding_min()], ",.2f")) + " units")

print("\nGood luck User, it seems pretty wet in your world.")
