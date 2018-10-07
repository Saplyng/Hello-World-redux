import UIKit

class Car{
    var topSpeed = 200

    func drive(){
        print("Driving at \(topSpeed)")
    }
}

class FutureCar : Car{

    override func drive(){

        super.drive()
        print("driving at \(topSpeed + 50)")
    }
    func fly(){
        print("flying")}
}

let myRide = Car()
myRide.topSpeed
myRide.drive()

let newRide = FutureCar()
newRide.topSpeed
newRide.drive()
newRide.fly()
