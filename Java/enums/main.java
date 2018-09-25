public class Main{
  enum Directions{
    EAST ("East", "E"),
    WEST ("West", "W"),
    NORTH ("North","N"),
    SOUTH ("South", "S");

    private final String shortDir;
    private final String properCase;

    Directions(String name, String code){
      this.properCase = name;
      this.shortDir = code;

    }

    public String getShortDir(){
      return this.shortDir;

    }
    public String getProperCase(){
      return this.properCase;
    }
  }

  
  public static void main(String args[]){
    Directions mydir = Directions.EAST;



    system.out.println(mydir.properCase);
  }
}
