import Foundation

print("Hello, World!")

var someArray = Array(repeating: 0, count: 10)
var animals = ["dog", "cat", "cow", "horse", "elephant", "penguin"]
animals[2] = "tiger"
print(animals)

var animalsLength = animals.count
print(animalsLength)

print(animals.contains("horse"))

var months = [1: "January",
              2: "February",
              3: "March",
              4: "April",
              5: "May",
              6: "June",
              7: "July",
              8: "August",
              9: "September",
              10: "October",
              11: "November",
              12: "December"]

let march = months[3]!
print(march)


let studentTuple: (Int, String) = (100682, "Ricky Rocket") // student id and name

var tupleArray = [(Int, String)]()

tupleArray.append(studentTuple)

print(tupleArray)


let numberSet: Set = [1, 2, 3, 1, 2, 4, 2, 5]
print(numberSet)
