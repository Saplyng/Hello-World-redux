
output_list = ['2', '2', '2', '3', '3', '3', '4', '4', '4', '5', '5', '5', '6',
               '6', '6', '7', '7', '7', '7', '8', '8', '8', '9', '9', '9', '9',
               '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '.']


input_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
              'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
              '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '.']


phone_number = input("type in a phone number: ")


phone_final = ""
for digit in phone_number:
    for item in range(0, len(input_list)):
        if digit.upper() == input_list[item]:
            phone_final += (output_list[item] + "")


print(phone_final)
