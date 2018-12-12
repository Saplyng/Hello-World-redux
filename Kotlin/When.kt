fun main(args: Array<String>) {

    print("Enter a number between 1 and 10 to know what it is in japanese: ")
    var number = readLine()!!
    var numString = "x"

    when(number){
        1 -> numString = "ichi"
        2 -> numString = "ni"
        3 -> numString = "san"
        4 -> numString = "shi"
        5 -> numString = "go"
        6 -> numString = "roku"
        7 -> numString = "nana"
        8 -> numString = "hachi"
        9 -> numString = "kyu"
        10 -> numString = "jyu"
        !in 1..10 -> numString = "Out of Range"
        "one" -> numString = "success"
        else -> numString = "Unknown"
    }

    println("the number $number is $numString in japanese")
}
