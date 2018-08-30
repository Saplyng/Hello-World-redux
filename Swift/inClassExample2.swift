let someValue = 2 + 5 + 37
type(of: someValue)
type(of: 3 + 4.0)

let doubleValue =44.&
type(of:doubleValue))
type(of:Double(someValue) + int(doubleValue))


// print will automatically round in obvious cases, such as repeating fraction
let numeric = 41.0 / 5.0
String(numeric)
print(numeric)
Int(numeric)

//string interpolation allows you to embed the String equvalent of a value
let iterpolated = "\(someValue) is an Int but \(Double(someValue)) is a Double"

//Ternary conditional operator takes a pattern like this
if someValue > 0{
  var result = "positive"
} else{
  var result = "negative"
}
result    // result is not defined in this SCOPE

//this is shorthand
var result = someValue > 0? "positive" : "negative"


// strings
var myString = "Triel en'Karnaca"

myString.count
myString.isEmpty
myString.lowercased()
myString.uppercased()


//unicode characters are expressed using 4 hex digits in curly braces preceded by \u
let fun = "\u{1404}\u{03DF}"
type(of: fun)

//a String is comprised of Characters
//a Character is an "extended grapheme CLuster" that is perceived as a single character
let twoGraphemes = "u\{65}\u{301}" //e + accent
let onGrapheme = "u\{E9" //also e + accent

twoGraphemes == oneGrapheme //outputs true


// strings use a data type to count character: String.INdex
var index = myString.startIndex
myString.insert("1", at: myString.endIndex)
