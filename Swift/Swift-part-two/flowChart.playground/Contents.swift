import UIKit
import PlaygroundSupport
PlaygroundPage.current.needsIndefiniteExecution = true


let startChoice = "fast" //options are "fast" or "right"
let startChoice2 = "right" //options are "fast" or "right"
let fastChoice = "no" //options are "no" and "almost"
let fastChoice2 = "almost" //options are "no" and "almost"
let doneChoice = "no" //options are "no" and "no..."
let doneChoice2 = "no..." //options are "no" and "no..."



func start(choice: String){
    print("project start")
    print("do things fast, or do things right?")
    switch choice{
    case "fast":
        print("fast")
        doesItWork(choice: fastChoice)
    case "right":
        print("right")
        areYouDone(choice: doneChoice2)
    default:
        print("Truly, are you even a programmer?")
    }
   
}


func doesItWork(choice: String){
    print("does it work yet?")
    switch choice{
    case "no":
        print("code fast")
        print("no")
        doesItWork(choice: fastChoice2)
    case "almost":
        print("almost, but it's become a mass of kludges and spaghetti code.")
        throwItOut()
    default:
        print("I guess giving up is an option too.")
        
    }
}

func areYouDone(choice: String){
    print("code well")
    switch choice{
    case "no":
        areYouDone(choice: doneChoice)
    case "no...":
        print("no, and the requirements have changed.")
        throwItOut()
    default:
        print("I guess giving up is an option too.")
    }
}

func throwItOut(){
    print("throw it all out and start over.")
    start(choice: startChoice2)
}


//very important
func goodCode(){
    print("?")
}



start(choice: startChoice)
