 import UIKit

 func fib(_ n: Int) -> Int {
    var number1 = 1
    var number2 = 1
    guard n > 1 else { return number1 }
    
    (2...n).forEach { _ in
        (number1, number2) = (number1 + number2, number1)
        print(number1)
    }
    return number1
 }
 
 fib(91)
