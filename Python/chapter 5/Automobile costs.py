initial_dialog = """
Hello again, User. Looks like you need to figure out how
much that car of yours is costing you, or as I like to call
them, "Wheely Money Holes"

Anyway, Just type in what I tell you and we'll be on our way...
"""


# as a warning, I don't really understand how functions work so I jsut
# did the code and pasted into a "function"
def main():
    print(initial_dialog)
    running_total = get_info()
    math_it_up(running_total)


# for, you know, getting the user's info
def get_info():

    money_holes = ['loan payment', 'insurance', 'gas', 'maintenance']
    running_total = []

# this was fun, so many layers, "i" is just a place holder variable
# it makes the user put in each of the integers for their differing bills
    for i in money_holes:
        while True:
            try:
                if i == money_holes[3]:
                    running_total.append(
                        int(input("what is your average monthly " + i + " bill? ")))
                    if not running_total[-1] >= 0:
                        del running_total[-1]
                        print(
                            "cmon don't screw with me, you're not paying negative money")
                        continue
                elif i != money_holes[3]:
                    running_total.append(
                        int(input("what is your monthly " + i + " bill? ")))
                    if not running_total[-1] >= 0:
                        del running_total[-1]
                        print(
                            "C'mon don't screw with me, you're not paying negative money")
                        continue
            except ValueError:
                print(
                    "You have to type a number not a letter, and no decimals, try again.")
                continue
            else:
                break
    return running_total


# math_it_up is designed to just do the math of the other funcion
# then print the result
def math_it_up(running_total):
    total_monthly_cost = sum(running_total)
    total_annual_cost = total_monthly_cost * 12

    print("\nThe total monthly cost of your expenses is: $" +
          str(format(total_monthly_cost, ",.2f")))
    print("The Approximate annual cost of your \"Wheely Money Hole\" is: $" +
          str(format(total_annual_cost, ",.2f")))


if __name__ == '__main__':
    main()
