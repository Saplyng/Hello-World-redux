initial_dialog = ("""Hello User, you must be an aspiring meteorologist!
that's the only reason I can think you would want something like
an average rainfall calculator.

But what would I know, I'm just a robot

Anyway, I wont burden you the hassle of converting your units, just be
consistent, if you start with Inches you better not change to Centimeters
by the end.

But since your too lazy to do some simple math yourself, I'm sure I won't
have to worry about that...

But what would I know, I'm just a robot\n""")

print(initial_dialog)

while True:
    try:
        user_years = int(input("How many years of data would you like to put in? "))
        if not user_years > 0:
            print("You're going to have to put in more years than 0")
            continue
    except ValueError:
        print("You have to type a number not a letter, try again.")
        continue
    else:
        break

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
rainfall_num = []

print("\nAlright, " + str(user_years) + " then, you'll have to")
print("type in all the numbers for each month")
print("I'll help count, by starting at zero (because I'm a computer)")
print("Try not to get lost.")

for num_years in range(user_years):
    print("\nThis is year " + str(num_years))
    for i in months:
        while True:
            try:
                rainfall_num.append(int(input(i + ": ")))
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
total_months = user_years * 12
average_rainfall = total_rainfall / total_months

print("\nTotal Months: " + str(total_months) + " months")
print("Total Rainfall: " + str(total_rainfall) + " units")
print("Average Rainfall per month over " + str(user_years) + " year(s): " + str(format(average_rainfall, '.2f') + " units"))

print("\nGood luck User, it seems pretty wet in your world.")
