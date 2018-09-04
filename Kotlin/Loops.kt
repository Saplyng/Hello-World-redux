const val LOOK_UP = 1
const val ADD = 2
const val CHANGE = 3
const val DELETE = 4
const val SHOW_DATABASE = 5
const val QUIT = 6

fun main(args: Array<String>) {
    var choice = 0
    while (choice != QUIT) {
        val customerMenu = """
  Supernatural Customer Email Lookup

  1 - look up a  customer
  2 - Add a new customer
  3 - change an email
  4 - delete a customer
  5 - show all customers
  6 - save and quit the program
  """
        println(customerMenu)
        println("Enter a number: ")
        choice = readLine()!!.toInt()

        if (choice == LOOK_UP)
            println("look up to be implemented later")
        else if (choice == ADD)
            println("add to be implemented later")
        else if (choice == CHANGE)
            println("change to be implemented later")
        else if (choice == DELETE)
            println("delete to be implemented later")
        else if (choice == SHOW_DATABASE)
            println("database to be implemented later")
        else if (choice == QUIT)
            println("quitting to to be implemented later, you live here now. JK")
    }
}
