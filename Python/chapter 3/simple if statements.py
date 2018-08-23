print("Hello once again user, today we've been instructed to play a numbers game!")
print(" ")
print("*INSERT CLAPPING HERE*")
from playsound import playsound
playsound('C:/Users/Sapli/Pictures/slow_clap.mp3')
print(" ")

print("It\'s quite simple User, all you have to do is pick a number")
print("between 1 and 7.")
print("If you don\'t, however, you'll make me sad. I might even cry a little,")
print("so please just pick one of those, okay?")

print(" ")

num_var = int(input("Alright let\'s get started, what number would you like?"))
print(" ")

if num_var == 1:
    print("Your number corresponds to Monday!")
elif num_var == 2:
    print("Your number corresponds to Tuesday!")
elif num_var == 3:
    print("Your number corresponds to Wednesday!")
elif num_var == 4:
    print("Your number corresponds to Thursday!")
elif num_var == 5:
    print("Your number corresponds to Friday!")
elif num_var == 6:
    print("Your number corresponds to Saturday!")
elif num_var == 7:
    print("Your number corresponds to Sunday!")
else:
    print("Q.Q")
    print("Why would you do that when I asked you not to?")
