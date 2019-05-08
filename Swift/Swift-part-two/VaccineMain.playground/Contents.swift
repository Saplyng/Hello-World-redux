import UIKit

let dateOfBirth = "2018-1-23"
let dateOfVaccine = "2018-4-15"
let userSearch = "Engerix-B"

//orderedVaccines()
//searchedVaccine(userSearch: userSearch)
//vaccineCalc(dateOfBirth: dateOfBirth, dateOfVaccine: dateOfVaccine)
public func main(userChoice: Int){
    let openingPrompt = """
    ***********************
    * Vaccine Application *
    *---------------------*
    *  Choose An Option:  *
    * 1. Search Vaccine   *
    * 2. Vaccine List     *
    * 3. Vaccine Calc     *
    ***********************

    """
    print(openingPrompt)

    switch userChoice {
    case 1:
        print("Chose: Search Vaccine \n")
        searchedVaccine(userSearch: userSearch)
    case 2:
        print("Chose: Vaccine List \n")
        orderedVaccines()
    case 3:
        print("Chose: Vaccine Calculator \n")
        vaccineCalc(dateOfBirth: dateOfBirth, dateOfVaccine: dateOfVaccine)
    default:
        print("Try a different number\n")
    }
}

main(userChoice: 3)
