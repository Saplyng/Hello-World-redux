import java.time.LocalDate
import java.time.format.DateTimeFormatter
import java.util.*

fun main(args: Array<String>) {
    val formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd")
    val today = LocalDate.now()
    val formattedToday = today.format(formatter)

    var newMoons: LocalDate = LocalDate.of(2018, 1, 1)

    fun correctedAverage(): Long{
        var moonAvg = 29.53
        fun moonMath(): Long{
            if (moonAvg >= 29.53) {
                moonAvg = (moonAvg + 29) / 2
                return 29
            }else if (moonAvg < 29.53) {
                moonAvg = (moonAvg + 30) / 2
                return 30
            }
            
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