print("Hello User! Sounds like you need to make some cookies")
print("but you dont know how much ingredients you need to make them,")
print("we\'ve all been there, but don\'t worry, I've got you covered")
print("Just tell me how many cookies you want!")

print(" ")

cookies_needed = int(input("How many cookies do you want?"))


sugar_base = float(1.5 / 48)
flour_base = float(2.75 / 48)
butter_base = float(1 / 48)

singular_cookie = sugar_base + flour_base + butter_base
multiple_cookies = singular_cookie * cookies_needed

sugar_needed = sugar_base * cookies_needed
flour_needed = flour_base * cookies_needed
butter_needed = butter_base * cookies_needed

print(" ")

print("Well then you're going to need " +
      str(round(sugar_needed, 2)) + " cups of sugar,")
print(str(round(butter_needed, 2)) + " cups of butter and " +
      str(round(flour_needed, 2)) + "cups of flour.")

print(" ")

print("Hoped that helped you User, save some cookies for me!")

print(" ")
input("HIT ENTER TO END")
