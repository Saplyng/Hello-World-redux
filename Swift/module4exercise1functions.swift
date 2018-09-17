//Module 4 Exercise 1 -- Functions

//For each of the numbered steps in the comments, add the code requested on the line(s) below the instruction.

import foundation

// 1. Create a function that takes an integer parameter and returns the square of the value. Call the function.
func square(x: Int) ->  Int {
  x = x * x
  return x
}

square()
// 2. Create a function that takes an Int, n, and returns the factorial of n as an optional Int. If n is negative, return nil. Call the function.
func factorial(factorialNumber: Double) -> Double {
    if factorialNumber == 0 {
        return 1
    } else {
        return factorialNumber * factorial(factorialNumber - 1)
    }
}


// 3. Create a function that takes an array of doubles as an argument and returns a tuple containing the sum of the array values and their average. Call the function.
func factorial(a: Int) -> Int {
    let n = a
    if(n == 1){
      return 1
    }else{
      return n*factorial(n-1)
    }
}

print(factorial(a: 7))

// 4. Create a function that takes a double score and returns a letter grade. Use an argument label for the argument. Call the function.


// 5. Create a generic function that takes a variadic parameter and returns an array holding all the elements passed in the parameter.
