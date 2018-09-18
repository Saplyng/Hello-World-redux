import java.time.LocalDate
import java.time.format.DateTimeFormatter
import java.util.*

fun main(args: Array<String>) {
    val formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd")
    val today = LocalDate.now()
    val formattedToday = today.format(formatter)

    var newMoons: LocalDate = LocalDate.of(1900, 1, 15)

    fun correctedAverage(): Long{
        var moonAvg = 29.53
        var result = 0
        fun moonMath(): Long{
            if (moonAvg > 29.53){
                moonAvg = (moonAvg + 29) / 2
                result = 29
            }else if (moonAvg <= 29.53){
                moonAvg = (moonAvg + 30) / 2
                result = 30
            }
            return result.toLong()
        }
        return moonMath()
    }

    while (newMoons.compareTo(today) < 0){
        newMoons = newMoons.plusDays(correctedAverage())
        //println(newMoons)
    }



    println("Today is $formattedToday")
    println("This is the next full moon $newMoons")
}
