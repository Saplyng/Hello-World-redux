while True:
    try:
        in_value = int(input("\n Enter a number (0 to quit)"))
        print(in_value, "times 5 is", in_value * 5)
        if in_value == 0:
            break
        else:
            print(in_value, "times 5 is", in_value * 5)
            continue


total = 0
count = 0
in_value = int(input("\nEnter a text score(-1 to quit)"))
while True:
    try:
        total += in_value
        count += 1
        continue
    else:
        break

average - total / count
print("\nFor", count, "scores")
