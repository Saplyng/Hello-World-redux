def main():  # so i'm starting to think main just acts like a key holder
    indulgence()


def indulgence():  # you know, because food
    cal_from_fat = fat_gram()
    cal_from_carb = carb_gram()
    cal_from_protein = protein_gram()
    print("\nYour calories from fat today are " +
          str(format(cal_from_fat, ",")))
    print("Your calories from carbs today are " +
          str(format(cal_from_carb, ",")))
    print("Your calories from proteins today are " +
          str(format(cal_from_protein, ",")))
    feelingfat()
    do_over()


def feelingfat():
    global total_calorie
    print("\nYour total amount of calories today is " +
          str(format(total_calorie, ",")))
    if total_calorie > 3000:
        print("You might wanna cut back on the twinkies.")


def catch_statement(macronutrient):
    while True:
        try:
            gram_count = int(
                input("How many " + macronutrient + " grams did you have today? "))
            if not gram_count >= 0:
                print("You didn't have less than 0 grams of " +
                      str(gram_count) + ", you can't lie!")
                continue
        except ValueError:
            print("That's not a number try again.")
            continue
        else:
            break
    return gram_count


total_calorie = 0


def fat_gram():
    fat = catch_statement('fat')
    cal_from_fat = fat * 9
    global total_calorie
    total_calorie += cal_from_fat
    return cal_from_fat


def carb_gram():
    carb = catch_statement('carb')
    cal_from_carb = carb * 4
    global total_calorie
    total_calorie += cal_from_carb
    return cal_from_carb


def protein_gram():
    protein = catch_statement('protein')
    cal_from_protein = protein * 4
    global total_calorie
    total_calorie += cal_from_protein
    return cal_from_protein


# new idea...need help with this
# giving the user option to start back from the beginning
def do_over():
    while True:
        yes_or_no = input(
            '\nDo you want to start over with a different day or person?(Y/N):')[0].lower()
        if yes_or_no == "y":
            main()
        else:
            print("Alright, see ya tomorrow")
            break


if __name__ == '__main__':
    main()
