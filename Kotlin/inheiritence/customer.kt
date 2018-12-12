open class Customer (
    customerName: String?,
    customerPhone: String?,
    customerAddress: String?,
    squareFootage: Int?){}

class Commercial (
    customerName: String?,
    customerPhone: String?,
    customerAddress: String?,
    squareFootage: Int?,
    propertyName: String?,
    multiProperty: Boolean): Customer(customerName, customerPhone, customerAddress, squareFootage){

        //calculating commercial rate as 0.5 cent per square foot. result in dollars
        // this makes the business person more money while the consumer feels less cheated
        

        fun information(){
            val commercialRate = (squareFootage * 0.5) / 100
            // decides wether they get 10% discount
            if( multiProperty == true){
                val weeklyCharge = commercialRate * 0.9
            }else{
                val weeklyCharge = commercialRate
            }   

             println("""
                Customer Name: $customerName
                Customer Phone Number: $customerPhone
                Customer Address: $customerAddress
                Multiple Customer properties: $multiProperty

                Property Name: $propertyName
                Property Square Footage: $squareFootage

                Weekly Charge: \$$weeklyCharge
                """
        
        
        )

        }

}





fun main(args: Array<String>){

    val whatever = Commercial("jimmy","123-456-7890", "something something", 14500, "mario's Pizzaria",true)
    whatever.information()
}