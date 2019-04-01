import UIKit


//user enters how many cookies they want
let cookies_needed: Double = 113.00

//cookie recipe: 1.5 cups, 2.75 cups, 1.0 cups of sugar flour and butter make 48 cookies
let sugar_base = Double(1.50 / 48.00)
let flour_base = Double(2.75 / 48.00)
let butter_base = Double(1.00 / 48.00)

let singular_cookie: Double = sugar_base + flour_base + butter_base
let multiple_cookies:Double = singular_cookie * cookies_needed

let sugar_needed: Double = sugar_base * cookies_needed
let flour_needed: Double = flour_base * cookies_needed
let butter_needed: Double = butter_base * cookies_needed

print("")

print("Well then you're going to need \((round(100*sugar_needed)/100)) cups of sugar,")
print("\((round(100*butter_needed)/100)) cups of butter and \((round(100*flour_needed)/100)) cups of flour.")

print(" ")

print("Hoped that helped you User, save some cookies for me!")

