def main():
    catch_statement()
    calc_average()
    determine_grade()


def calc_average():
    global grades
    grades = sum(grades)
    grades /= 5
    print("\nYour overall average was: " + str(grades))


def determine_grade():
    global grades
    if grades >= 90:
        print("you got an A")
    elif 80 <= grades <= 89:
        print("you got a B")
    elif 70 <= grades <= 79:
        print("you got a C")
    elif 60 <= grades <= 69:
        print("you got a D")
    else:
        print("You failure, you got an F")


def catch_statement():
    for i in grade_input:
        while True:
            try:
                grades.append(int(input("What is your " + i + " score?: ")))
                if not grades[-1] >= 0:
                    del grades[-1]
                    print("I don't think your number was quite right, try again")
                    continue
                if grades[-1] > 100:
                    del grades[-1]
                    print("You cant have more than 100 on your tests, don't try to cheat me!")
                    continue
            except ValueError:
                print("You have to type something different that")
                continue
            else:
                break


grade_input = ['first', 'second', 'third', 'fourth', 'fifth']
grades = []

if __name__ == '__main__':
    main()
