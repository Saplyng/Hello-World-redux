fun main(args: Array<String>) {
//    val temperature = 92.0..104.0
//    val low = -459.67..97.4
//    val normal = 97.5..99.5
//    val high = 99.6..1800.0

    while(true) {
        print("Please enter your Humans temperature for evaluation: ")

        val actualTemp = readLine()!!.toDouble()

        if (actualTemp > 104.0)
            println("Your Human is most likely dying or dead of heat, please seek additional medical assistance.")
        else if (actualTemp < 92.0)
            println("Your Human is most likely dying or dead from cold, please seek additional medical assistance.")

        else if (actualTemp >= 92.0 && actualTemp < 97.5)
            println("Your human is too cold, it needs immediate medical assistance to prevent death")

        else if (actualTemp <= 1800.0 && actualTemp > 99.5)
            println("Your Human is too hot, it needs immediate medical assistance to prevent death")

        else if (actualTemp <= 99.5 && actualTemp >= 97.5)
            println("Your Human is within appropriate temperature parameters, please pay mandatory 100 credits")

        else
            println("Error")
            break


    }
}
