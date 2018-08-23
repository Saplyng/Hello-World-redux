# library
roman_numerals = {'1': 'I',
                  '2': 'II',
                  '3': 'III',
                  '4': 'IV',
                  '5': 'V',
                  '6': 'VI',
                  '7': 'VII',
                  '8': 'VIII',
                  '9': 'IX',
                  '10': 'X'}

startup_dialog = """Ave, User! Welcome to Roman Numerology \"CI\" (or 101)!

Today we're going to be starting with the basics, as such
you're going to need to know how to count from the beginning.
1-10 will get you 80% of the way through our numbering system
so you should familiarize yourself with those first.
"""


print(startup_dialog)

# this was the complicated bit, very hard to understand, well, for me...


def conversion(number):
    converted_number = roman_numerals[number]
    print(' ')
    print('The Roman equivalent is {}'.format(converted_number))


# had to look up a way to make sure that i was getting no errors
while True:
    try:
        user_number = int(input("Pick a number 1 through 10 :"))
    except ValueError:
        print("There's a time and place for everything but not now.")
        continue
    else:
        break


if 0 < user_number < 11:
    conversion(str(user_number))
else:
    print(" ")
    print("We have no time for your tomfoolery, this is a learned")
    print("society, get out of my class!")
