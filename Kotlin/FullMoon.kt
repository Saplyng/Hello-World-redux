import java.time.LocalDate
import java.time.format.DateTimeFormatter
import java.util.*

fun main(args: Array<String>) {
    var average = 29.53
    var year: Int = Calendar.getInstance().get(Calendar.YEAR)
    val formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd")
    var today = LocalDate.now()
    val formattedToday = today.format(formatter)

    var newMoons: LocalDate = LocalDate.of(2018, 1, 1)

    while (newMoons.compareTo(today) < 0){
        newMoons = newMoons.plusDays(30)
        //println(newMoons)
    }

    fun avg(args: Int){
      if (average >= 29.53){
        average = (average + 29) / 2
        return 29
      else if (average < 28.53){
        average = (average + 30) / 2
        return 30
      }
      }
    }

    println("Today is $formattedToday")
    println("This is the next full moon $newMoons")




}
