import java.time.LocalDate
import java.time.format.DateTimeFormatter
import java.time.temporal.ChronoUnit
import java.util.*

fun main(args: Array<String>) {
    var year: Int = Calendar.getInstance().get(Calendar.YEAR)
    val formatter = DateTimeFormatter.ofPattern("MM/dd/yyyy")
    var today = LocalDate.now()
    val formattedToday = today.format(formatter)

    println("\nToday is $formattedToday")

    println("\nEnter your birth month: ")
    var birthMonth: Int = readLine()!!.toInt()

    println("\nEnter your birth day: ")
    var birthDay: Int = readLine()!!.toInt()

    var holdBirthday: LocalDate = LocalDate.of(year,birthMonth,birthDay)


    //println("${holdBirthday.isBefore(today)}")
    if (holdBirthday.isBefore(today)){
        //println("$holdBirthday")
        holdBirthday = holdBirthday.plusYears(1)
        //println("$holdBirthday")
    }

    val nextBirthday = holdBirthday.format(formatter)

    var daysToBirthday = today.until(holdBirthday, ChronoUnit.DAYS)

    if (daysToBirthday.toInt() == 0){
        println("\nHappy Brithday!")
    } else {
        println("\nYou next birthday is: $nextBirthday and there are $daysToBirthday day(s) until then!")
    }




}
