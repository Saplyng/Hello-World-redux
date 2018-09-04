import java.util.Scanner;

public calss main {
  public static void main(String[] args){

    int nUserNum1, nUserNum2, nUserNum3 = 0;
    int nResult = 0;

    nUserNum1 = getInput(sLabel: "Enter a number: ");
    nUserNum2 = getInput(sLabel: "Enter another number: ");
    nUserNum3 = getInput(sLabel: "Enter a third number: ");
    nResult = bigger(nUserNum1, nUserNum2, nUserNum3);
    System.out.println("the numbers are: " + nUserNum1 + " and " + nUserNum2 + " and " + nUserNum3);
    System.out.println(nResult + " is bigger.");


  }

  public static int getInput(String sLabel){
    int nItem = 0
    Scanner sc = new Scanner(System.in);
    System.out.print(sLabel);
    nItem = sc.nextInt();
    return nItem;

  }

  public static int bigger(int num1, int num2){
    int result = 0;
    if(num1 > num2)
      result = num1;
    else
      result = num2;

    return result;
  }

  public static int bigger(int num1, int num2, int num3){
    int result = 0;
    if(num1 > num2 && num1 > num3)
      result = num1;
    else if (num2 > num1 && num2 > num3)
      result = num2;
    else
      result = num3;
    return result;
  }

  public static void arrayTest(){
    int[] aNumber; // declaration
    aNumber = new int[10]; // init

    // int[] aNumber1 = new int[10];
    // int aNumber[] = new int[10];

    aNumber[0] = 5;
    aNumber[1] = 10;

    for(int i = 0; i < aNumber.length; i++){
      System.out.prinln("Array element is: " + aNumber[i]);
    }
  }
  public static void dblArray(){
    int[][] aMultiArray = new int [5][6];
    aMultiArray[3][4] = 50;
  }
}
