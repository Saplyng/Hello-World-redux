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
            2 -> payRate = (payRate * 1.05)
            3 -> payRate = (payRate * 1.10)
            else -> {
                print("Error, employee doesnt have shift 1, 2, or 3")}}

        var moneyMade = hoursIn * payRate

        //calculation for overtime
        if(hoursIn > 40 &&  !salary){
            var overtimeHours = hoursIn - 40
            var OvertimePay = ((overtimeHours * (payRate * 1.50)))
            moneyMade = 40 * payRate
            actualPay = moneyMade + OvertimePay
            println(OvertimePay)
        }else{
            actualPay = moneyMade
        }


        //output displayed from calculate function
         print(
            """
                |employee name: $name
                |employee position : $position
                |employee salary : $salary
                |employee pay rate : $${"%.2f".format(payRate)}/hr
                |Shift number: $shift
                |money earned this week: $${"%.2f".format(actualPay)}
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



fun main(args: Array<String>) {


    var wanda = Employee("Wanda", PositionTitle.ADMINISTRATION, false, 10.00, 1, "2018-2-28")


     wanda.calculate(41.00)

}
