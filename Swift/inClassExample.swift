//single line comment
/*
 multi-line comment
 */

let theAnswer = 42 // inferred type
let inferredDouble = 42.1
let declaredFloat: Float = 42.1

type(of: theAnswer)

let floatEqualsDouble = inferredDouble == Double(declaredFloat)
type(of: inferredDouble)
type(of:declaredFloat)
type(of:Double(declaredFloat))

let 🦊 = "fox"
let 🐷 = "pig"


var a = 6; var b = 7 //statements seperated by ;
//built in data types
Int.max
Int8.max
Int16.max
Int32.max
Int64.max

UInt8.max    //unsigned



//tuples

let labeledTuple = (first: 1.0, second: 3.5, third:6.0, fourth: 7)
labeledTuple.second

let dataPoint = (1.2, 3.4, 7.9)
dataPoint.0 // can reference by position in the tuple

var(x,y,z) = dataPoint
x
y
z

x = (y+z) * x
dataPoint
dataPoint.0

var url = ("mchenry","instruction","com", 333)

let userChoice: String     //create a constracnt with no value, but need type
userChoice = "Tset"



// optional may or may not currently have value


let optionalString: String?   //no value yet
optionalString = "hello"
print(optionalString as Any)
print(optionalString!)      // ! to unwrap the value


var optionalNumber: Int?
optionalNumber = 7

//even though it has a value, it's still an optional
//it still needs to be unwrapped
optionalNumber!     // forced unwrapping is the ! -- only if i know it has a value other wise error

//test for nil
if optionalNumber != nil{
    print(optionalNumber!)
}

// i can also use optional binding like this
// optional binding will unwrap AND assign ONly if not nil
if let num = optionalNumber{
    print(num)
} else{
    print("optionalNumber has no value")
}

// you will see this in iOS apps
//IMPLICITLY UNWRAPPEDS OPTIONAL
//the optional is unwrapped at the same time is is declared

var unwrappedString: String!
//you see this in apps where the initializtion of the optional
//occurs before you are given access to the variable
