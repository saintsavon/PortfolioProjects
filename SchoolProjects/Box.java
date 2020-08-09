package SchoolProjects;

public class Box {

    int size = 0;

    public void printBox() {

        for (int row=0; row<size; row++) {
            for (int col=0; col<size; col++) {
                System.out.print("*");
            }
            System.out.println();
          }
    }

    public void printBox(char c) {
        
          for (int row=0; row<size; row++) {
                 for (int col=0; col<size; col++) {
                     System.out.print("c");
                 }

                 System.out.println();
          }
    }

 public static void main(String[] args) {

    Box b1 = new Box();
    b1.size = 5;
    b1.printBox();
    Box c = new Box();
    c.size = 5;
    c.printBox('c');

    }
}