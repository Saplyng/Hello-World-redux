import UIKit
import Foundation


public func vaccineCalc(dateOfBirth: String, dateOfVaccine: String){

    //date formatter, structured in ISO8601, locale doesnt seem to be working(?)
    let dateFormat = DateFormatter()
    dateFormat.dateFormat = "yyyy-MM-dd"
    dateFormat.locale = Locale(identifier: "en_US_POSIX")


    let now = Date()
    let formatNow = dateFormat.string(from: now)



    //taking user constants(Strings) and formatting them to Dates, fatal error if wrong
    guard let idDateOfBirth = dateFormat.date(from:dateOfBirth) else {
        fatalError()
    }
    guard let idDateOfVaccine = dateFormat.date(from:dateOfVaccine) else {
        fatalError()
    }

    //print(dateFormat.string(from:idDateOfBirth))


    //Date math goes here
    let idAge = Calendar.current.dateComponents([.year, .month], from: idDateOfBirth, to: now)
    let idAgeAtVaccine = Calendar.current.dateComponents([.year, .month], from: idDateOfBirth, to: idDateOfVaccine)
    let idTimeSinceVaccine = Calendar.current.dateComponents([.year, .month], from: idDateOfVaccine, to: now)


    //output for the User
    print("Today is \(formatNow)")
    print("Patient Age: \(idAge.year!) years \(idAge.month!) months old")
    print("Age at Vaccine: \(idAgeAtVaccine.year!) years \(idAgeAtVaccine.month!) months old")
    print("Time since Vaccination: \(idTimeSinceVaccine.year!) years \(idTimeSinceVaccine.month!) months old")
}
