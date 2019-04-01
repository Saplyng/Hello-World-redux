import UIKit



//what we are going to do is make all ingredients a bunch of functions that add to the total
//price. then when the user wants to end they can use the "confirm" function to get the total of
//the meal



protocol Ingredients{
    var price: Double { get set }
    var ingredientList: Array<String> {get set}
    
    mutating func pickles() -> Any
    mutating func tomatoes() -> Any
    mutating func onions() -> Any
    mutating func meatPatty() -> Any
    mutating func cheese() -> Any
    mutating func end() -> Any
}

struct Burger: Ingredients{
    var price: Double = 5.00
    var ingredientList = [String]()
    init(){
        price = 5.00
        ingredientList = []
    }
    
    mutating func pickles() -> Any {
        self.price += 0.10
        ingredientList.append("pickles")
        return print("added")
    }
    
    mutating func tomatoes() -> Any {
        self.price += 0.20
        ingredientList.append("tomatoes")
        return print("added")
    }
    
    mutating func onions() -> Any {
        self.price += 0.20
        ingredientList.append("onions")
        return print("added")
    }
    
    mutating func meatPatty() -> Any {
        self.price += 1.00
        ingredientList.append("patty")
        return print("added")
    }
    
    mutating func cheese() -> Any {
        self.price += 0.25
        ingredientList.append("cheese")
        return print("added")
    }
    mutating func end() -> Any {
        return print("You ordered a Burger with: \(ingredientList). The total is $\(price)")
    }
}

enum Food{
    case pickles, tomatoes, onions, meatPatty, cheese, end
}




//user decides
var choice = Food.meatPatty

var newBurger = Burger()

switch choice {
case .pickles:newBurger.pickles()
    print("pickles added to burger")
    print(newBurger.price)
case .tomatoes:newBurger.tomatoes()
    print("tomatoes added to burger")
    print(newBurger.price)
case .onions:newBurger.onions()
    print("onions added to burger")
    print(newBurger.price)
case .meatPatty:newBurger.meatPatty()
    print("meat added to burger")
    print(newBurger.price)
    print(newBurger.ingredientList)
case .cheese:newBurger.cheese()
    print("cheese added to burger")
    print(newBurger.price)
case .end:newBurger.end()
    print("order ended")
    print(newBurger.price)
}

