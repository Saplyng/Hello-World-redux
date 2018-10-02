class Person{
    String name;

    public Person(String name){
        this.name = name;
    }
}

class Mother extends Person{
    Mother(String n){
        super(n);
        name = "Mother: " + n;
    }
    void FeedChildren(){
        System.out.prinln(name + "has fed the kids.");
    }
}

class Wife extends Person {
    Wife(String n){
        super(n);
        name = "Wife: " + n;

    }

    void CallHusband(){
        System.out.println(name + " is calling - RUN!");
    }
}


public class Main{
    public static void main (String args[]){
        Person p = new Person("julie");
        Mother m = new Mother("Mary");
        Wife w = new Wife("Jill");
        System.out.println("p is - " + p.name);
        System.out.println("p is - " + m.name);
        System.out.println("p is - " + w.name);
        m.FeedChildren();
        w.CallHusband();
    }
}
