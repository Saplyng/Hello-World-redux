class Employee (
        var name : String,
        var position : PositionTitle,
        var salary : Boolean,
        var payRate : Double,
        var shift : Int?,
        val startDate : String?){



    var actualPay = 0.00

    fun calculate(hoursIn: Double){
        when(shift){
            1 -> payRate = payRate
            2 -> payRate = payRate * 1.05
            3 -> payRate = payRate * 1.10
            else -> {

             print("Error, employee doesnt have shift 1, 2, or 3")}}



        if(hoursIn > 40 &&  !salary){
            actualPay = payRate * 1.50
        }else{
            actualPay = payRate
        }



         print(
            """
                |employee name: $name
                |employee position : $position
                |employee salary : $salary
                |employee pay rate : $payRate
                |Shift number: $shift
                |money earned this week: $actualPay
                """.trimMargin())

    }

    fun printAll(){
        println(
                """
                |employee name: $name
                |employee position : $position
                |employee salary : $salary
                |employee pay rate : $payRate
                |Shift number: $shift
                |money earned this week: $actualPay
                """.trimMargin())}


}

enum class PositionTitle{
    ADMINISTRATION, PRODUCTION, SALES, MAINTENANCE, TECHNICAL, SECRETARIAL
}


class Main {
    fun main(args: Array<String>) {


        var wanda = Employee("Wanda", PositionTitle.ADMINISTRATION, true, 50.00, 3, "2018-2-28")


        wanda.calculate(45.00)

    }


}
