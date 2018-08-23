def main():
    catch_statement()
    getting_initials()
    printing_initials()


def catch_statement():
    for i in name_parts:
        while True:
            try:
                user_name.append((input("What is your " + i + " name?: ")))
            except ValueError:
                print("I don't think your name is a number, try again")
                continue
            else:
                break


name_parts = ('first', 'middle', 'last')
user_name = []
user_initials = []


def getting_initials():
    for f in user_name:
        global user_initials
        user_initials += f[0]


def printing_initials():
    global user_initials
    user_initials = [element.upper() for element in user_initials]
    print(str(user_initials[0]) + '.' +
          str(user_initials[1]) + '.' + str(user_initials[2]))


if __name__ == '__main__':
    main()
