import Foundation

func paintJob(squareFeet: Int,paintCost: Double) -> String {
    let paintRequired = (Double(squareFeet) / 380).rounded(.up) // amount(gallons) of paint for the project
    
    let paintTotal = paintCost * paintRequired // total cost of all the paint required
    
    let sqFootPerHour = 47.5 //can finish 47.5 sq per hour
    let laborRequired = (Double(squareFeet) / sqFootPerHour) //hours of labor requred
    let laborCharge = 35.00 * laborRequired // labor charges
    
    var totalCharge = laborCharge + paintTotal
    totalCharge = Double(round(100*totalCharge)/100) // format to two decimal places
    
    
    let printOutString = """
  Paint Job Estimation
  
  Estimated time to completion: \(laborRequired)
  Labor cost at $35.00 per hour: $\(laborCharge)
  
  Gallons of paint required: \(paintRequired) Gallons
  Paint cost at $\(paintCost) per gallon: $\(paintTotal)
  
  Grand total estimated cost for job: $\(totalCharge)
    (based on \(squareFeet) total square feet.)
  """
    return printOutString
    
}

print(paintJob(squareFeet: 5000, paintCost: 25.00))
