public class Main {

    public int addIt(int num1, int num2){
        /**
        *
        *@param num1
        *@param num2
        *@return the sum of two numbers
        */
        return (num1 + num2)
    }
    /**
    *
    *name: main
    *@author: Dave Boesen
    *@param args Takes input from cmd line
    *@throws Exception only if i messed up
    *10/2/18 DMB modified the main program added if i messed up
    *
    */
    public static void main(String args [])throws Exception{
        String sTest = "the quick brown fox jumped over the lazy dog";
        String[] sArray = sTest.split(" ");
        String sTestError = "";
        Boolean bImessedUp = true;

        try{
            if (bImessedUp){
                throw new Exception("This is me messing up.");
            }
            // for (String x: sArray){
            //     system.out.println(x);
            // }

            sTestError = sArray [32];
            System.out.println(sTestError);
        }catch (ArrayIndexOutOfBoundsException e) {
            sTestError = sArray[0];
            System.out.println("The index is out of bounds");
        }catch (Exception e){
            switch(e.getMessage()){
                case "This is me messing up.":
                System.out.println(e.getMessage());
                break;
            }
            e.printStackTrace();
        }finally{
            //close streams, databases, etc...

        }
        System.out.println("TestError: " + sTestError);
        System.out.println("Outside of the try and catch statement");
    }
}
