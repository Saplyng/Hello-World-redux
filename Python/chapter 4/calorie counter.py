data = [10, 15, 20, 25, 30]
calories_burned = [10, 15, 20, 25, 30]

for data, calories_burned in zip(data, calories_burned):

    calories_burned *= 4.2
    print('The calories burned in ' + str(data) +
          ' minutes are: ' + str(calories_burned))
