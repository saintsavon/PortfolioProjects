package SchoolProjects;

import java.util.*;

public class Lift{

    public static void main(String[] args){

        int m, n;
        int k;
        int c = 0;
        Scanner sc = new Scanner(System.in);

        while(true){
           System.out.println("1. Operate the elevator");
           System.out.println("2. Quit");

           if (c == 0)
              System.out.println("The elevator is at the basement");

           else {
              System.out.println("The elevator is at floor " + c );

           }

           System.out.print("Enter your choice:");
           k = Integer.parseInt(sc.nextLine());

           if (k == 2){
              break;

           }

           if (k == 1){
              System.out.print("Which floor are you at? (0,1,2):"); // 0- Basement
              n = Integer.parseInt(sc.nextLine());
              int valid = 0;
              System.out.print("Which floor do you want to go:");
              m = Integer.parseInt(sc.nextLine());

              if (c == 0)
                 System.out.println("The elevator is at the basement");

              else {
                 System.out.println("The elevator is at floor " + c );

              }

              if (c == n){
                 System.out.println("The elevator is now open");

                 if (m > c){
                    System.out.println("The elevator is going up");
                    System.out.println("The elevator is now at floor" + m );

                    c = m;

                 }

                 if (m < c){
                    System.out.println("The elevator is going down");
                    System.out.println("The elevator is now at floor " + m );

                    c = m;

                 }

              }

              else {

                 if (n > c){
                    System.out.println("The elevator is going up");
                    System.out.println("The elevator is now at " + n);
                    System.out.println("The elevator is now open");
                    System.out.println("The elevator is now closed");

                    c = n;

                    if (m > c){
                       System.out.println("The elevator is U");
                       System.out.println("The elevator is now at floor " + m );
                       System.out.println("The elevator is open");

                       c = m;

                    }

                    if (m < c){
                       System.out.println("The elevator is going down");
                       System.out.println("The elevator is now at floor " + m );
                       System.out.println("The elevator is open");

                       c = m;

                    }

                 }               

              }             

           }

        }

    }

}

