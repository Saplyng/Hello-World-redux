fun main(args: Array<String>) {

    fun triangle(){
        println("enter Length: ")
        val length = readLine()!!.toDouble()
        println("enter width: ")
        val width = readLine()!!.toDouble()
        val sum = (length * width) / 2
        println("Area is " + sum)
    }

    fun rectangle(){
        println("enter Length: ")
        val length = readLine()!!.toDouble()
        println("enter width: ")
        val width = readLine()!!.toDouble()
        val sum = (length * width)
        println("Area is " + sum)
    }

    fun trapezoid(){
        println("enter first Length: ")
        val length1 = readLine()!!.toDouble()    
        println("enter second Length: ")
        val length2 = readLine()!!.toDouble()
        println("enter Height: ")
        val height = readLine()!!.toDouble()
        val sum = 0.5 * (length1 + length2) * height
        println("Area is " + sum)
    }

    fun elipse(){
        println("enter first Radius: ")
        val radius1 = readLine()!!.toDouble()
        println("enter second Radius: ")
        val radius2 = readLine()!!.toDouble()
        val sum = 3.14 * radius1 * radius2
        println("Area is " + sum)
    }

        val customerMenu = """
  Quick Area calculator

  1 - Triangle
  2 - Rectangle
  3 - Trapezoid
  4 - Elipse
  """
    println(customerMenu)
    println("Enter a number: ")
    val x = readLine()!!.toInt()
    when(x){
        1 -> triangle()
        2 -> rectangle()
        3 -> trapezoid()
        4 -> elipse()
        else -> print("Not Available")
    }
    //println("have a nice day")
}