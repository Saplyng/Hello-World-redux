def main():  # just open program and start it, don't do too much
    transition_func()


def transition_func():  # ideally will hold the rest of the functions
    a_variable_name = [opening_file()]
    print(a_variable_name)


# This is where i'm having an issue with, i'm not sure how to get num_list
# out so that I can use it elsewhere
def opening_file():
    while True:
        try:
            num_list = open('numbers.txt', 'r')
            for number in num_list:

            return num_list
        except IOError as e:
            print("IOError: We couldn't open your file: ", e)
            break


# simple appending thingy, it's doing it's job properly I believe
def appending(variable_thing):
    global adding_total
    while True:
        try:
            for i in variable_thing:
                adding_total.append(int(i))
        except ValueError as e:
            print("There was an error with your data: ", e)
            break


# simple math thingy, it is also doing it's job well
def doing_the_math():
    amount_in_list = len(adding_total)
    total_num = sum(adding_total)
    average_num = total_num / amount_in_list
    print("Here's the total number for everything in numbers.txt: " +
          format(total_num, ',.2f'))
    print("Here's the average number for everything in numbers.txt: " +
          format(average_num, ',.2f'))


adding_total = []  # the variable that the appending function is using


if __name__ == '__main__':
    main()
