open class Customer(
    var customerName: String,
    var customerPhone: String,
    var customerAddress: String,
    var squareFootage: Int
){}

class Commercial(
    var propertyName: String,
    val commercialRate: 5,
    var multiProperty: boolean
) : Customer(customerName,
            customerPhone,
            customerAddress,
            squareFootage){

    fun charge(){
        
    }



}

        