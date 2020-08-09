package SchoolProjects;

Driver.java

public class Driver {

    public static void main(String args[]) {

        //creating instances
        ArrayStack obj1 = new ArrayStack();
        System.out.println("Pushing 1,7,3,4,9,2");
        obj1.push(1);
        obj1.push(7);
        obj1.push(3);
        obj1.push(4);
        obj1.push(9);
        obj1.push(2);
        System.out.println("After pushing data, the size of arraystack is  " +obj1.size());
        obj1.pop(); obj1.pop(); obj1.pop(); obj1.pop(); obj1.pop();  obj1.pop();
        System.out.println("After popping data, the size of arraystack is " +obj1.size());

        //LInkedStack
        LinkedStack obj2 = new LinkedStack();
        System.out.println("Pushing 1,7,3,4,9,2");
        obj2.push(1);
        obj2.push(7);
        obj2.push(3);
        obj2.push(4);
        obj2.push(9);
        obj2.push(2);
        System.out.println("After pushing data, the size of linkedstack is  "+obj2.size());
        System.out.println(obj2);

        //Pop
        obj2.pop(); obj2.pop(); obj2.pop(); obj2.pop(); obj2.pop(); obj2.pop();
        System.out.println("After popping data, the size of linkedStack is  "+obj2.size());
        System.out.println(obj2);

    }

}