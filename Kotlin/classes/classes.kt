class Employee (
        var firstName : String?,
        var lastName : String?,
        var number : String?,
        var shift : Int)
{
    fun printAll(){
        println(
                """
                |employee Number: $number
                |employee name: $firstName $lastName
                |Shift Number: $shift
                """.trimMargin())}
}


fun main(args: Array<String>){


    val jimmy = Employee("Jimmy", "juelianne", "1",1)
    val ricky = Employee("Ricky", "Rickardo", "2",3)
    val lucy = Employee("Lucy", "Longinous", "3",2)

    println()
    jimmy.printAll()
    println()
    ricky.printAll()
    println()
    lucy.printAll()


    // jimmy got his name changed
    jimmy.firstName = "Johnny"
    println()
    jimmy.printAll()
}
