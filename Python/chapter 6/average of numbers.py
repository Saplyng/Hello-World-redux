def main():
    opening_and_appending()
    doing_the_math()


def opening_and_appending():
    num_list = open('numbers.txt')
    global adding_total
    for i in num_list:
        adding_total.append(int(i))


def doing_the_math():
    amount_in_list = len(adding_total)
    total_num = sum(adding_total)
    average_num = total_num / amount_in_list
    print("Here's how many items were in numbers.txt: " +
          format(amount_in_list, ',.2f'))
    print("Here's the total number for everything in numbers.txt: " +
          format(total_num, ',.2f'))
    print("Here's the average number for everything in numbers.txt: " +
          format(average_num, ',.2f'))


adding_total = []


if __name__ == '__main__':
    main()
