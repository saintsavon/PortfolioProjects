package SchoolProjects;

import java.util.Scanner;

public class EvenNumSum {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int UserInput;
        int EvenSum;
        int avg;
        int FinalSum;

        System.out.println("Please enter an integer > 2.");

        UserInput = scan.nextInt();

        while (UserInput < 2) {
            System.out.println("Please enter a valid integer, and try again.");

            UserInput = scan.nextInt();

        continue; // allows user to input multiple times until integer entered is valid
        }

        avg = ((UserInput+2)/2) - 1;
        FinalSum = (avg+1);  // equation used = N(N+1)
        EvenSum = (avg*FinalSum);

        System.out.println(EvenSum);
       }
}