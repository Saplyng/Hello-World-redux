public class Person{
  String firstName = "";
  String lastName = "";
  String address = "";
  String city = "";
  String state = "";
  String zipCode = "";
  String hmPhone = "";
  String celPhone = "";
  LocalDate birthdate = LocalDate.now();


  public static int calcAge(LocalDate xDate){
    return xDate.until(LocalDate.now(), ChronoUnit.DAYS);
  }












}
