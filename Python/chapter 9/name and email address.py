# Write a program that keeps names and email addresses in a dictionary as
# key-value pairs. THe program should display a menu that lets the user look up
# a person's email address, add a new name and email address, change an
# existing email address, and delete an existing name and email address. The
# program should pickle the dictionary and save it to a file when the user
# exits the program. Each time the program starts, it should retrieve the
# dictionary from the file and unpickle it.


import pickle

LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
SHOW_DATABASE = 5
QUIT = 6


def main():
    try:
        input_file = open("customer_file.dat", 'rb')
        customers = pickle.load(input_file)
        # print(customers)
    except (FileNotFoundError, IOError):
        print("file not found, please add a customer then quit to create the file")
        customers = {}
    # choice
    choice = 0

    while choice != QUIT:
        # get the user's menu choice
        choice = menu()
        # process the choice
        if choice == LOOK_UP:
            look_up(customers)
        elif choice == ADD:
            add(customers)
        elif choice == DELETE:
            change(customers)
        elif choice == SHOW_DATABASE:
            show_data(customers)
        elif choice == QUIT:
            save(customers)


def menu():
    customer_menu = """
    Supernatural Customer Email Lookup

    1 - look up a  customer
    2 - Add a new customer
    3 - change an email
    4 - delete a customer
    5 - show all customers
    6 - save and quit the program
    """
    print(customer_menu)
    choice = int(input("Enter a number:  "))
    while choice < 1 or choice > 6:
        choice = int(input("\nCmon, enter a real choice"))
    return choice


# look up a customer
def look_up(customers):
    name = input("Enter the Customer's name:  ")
    print(customers.get(name, "Customer not Found"))


# add a customer
def add(customers):
    # check to see if customer exists, then add customer
    name = input('Enter customer name:  ')
    email = input("Enter customer's email address:  ")
    if name not in customers:
        customers[name] = email
        print("customer added")
    else:
        print("That entry already exists.")


# change a customer's email
def change(customers):
    name = input("Enter the customer name:  ")
    if name in customers:
        email = input("enter the new email address:  ")
        customers[name] = email
    else:
        print("That customeris not found.")


# delete a customer's
def delete(customers):
    name = input("enter the customer name:  ")
    if name in customers:
        del customers[name]
    else:
        print("That customer was not found. ")


def show_data(customers):
    for customer in customers:
        print(customer, "   :   ", customers[customer])


# save the data and close the program
def save(customers):
    print("The data file has been overwritten and saved")
    save_file = open('customer_file.dat', 'wb')
    pickle.dump(customers, save_file)
    save_file.close()
    print("See ya next time Space Cowboy")


main()
