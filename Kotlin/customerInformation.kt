fun main(args: Array<String>){

    fun customerInfo(name: String, phoneNumber: String){

        println("")
        println("$name \n$phoneNumber")
        println("")
        println("thank you")

    }

    fun customerInfo(businessName: String, contactName: String, phoneNumber: String){

        println("")
        println("$businessName \n$contactName \n$phoneNumber")
        println("")
        println("thank you")
    }

    var informationList: MutableList<String> = mutableListOf<String>()
    val customerMenu = """
  Please enter the number of your selection

  1 - Residential Customer
  2 - Business Customer
  """
    println(customerMenu)
    println("Enter a number: ")
    val x = readLine()!!.toInt()
    when(x){
        1 -> {  println("enter name: ")
                informationList.add(readLine()!!.toString())
                println("enter phone number: ")
                informationList.add(readLine()!!.toString())
                customerInfo(informationList[0],informationList[1])
            }
        2 -> {  println("enter business name: ")
                informationList.add(readLine()!!.toString())
                println("enter contact name: ")
                informationList.add(readLine()!!.toString())
                println("enter phone number: ")
                informationList.add(readLine()!!.toString())
                
                customerInfo(informationList[0],informationList[1],informationList[2])
            }
        else -> print("not Available try again")
    }


}