import java.time.LocalDate
import java.time.format.DateTimeFormatter
import java.util.*

fun main(args: Array<String>) {
    var year: Int = Calendar.getInstance().get(Calendar.YEAR)
    val formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd")
    var today = LocalDate.now()
    val formattedToday = today.format(formatter)

    var newMoons: LocalDate = LocalDate.of(2018, 1, 1)

    while (newMoons.compareTo(today) < 0){
        newMoons = newMoons.plusDays(30)
        //println(newMoons)
    }


    println("Today is $formattedToday")
    println("This is the next full moon $newMoons")




}