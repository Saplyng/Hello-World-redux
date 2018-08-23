def main():
    read_name()


def read_name():
    i = open('names.txt')
    name_num = 0
    for name in i:
        name_num = name_num + 1
        print(str(name_num) + '    ' + name, end='')


if __name__ == '__main__':
    main()
