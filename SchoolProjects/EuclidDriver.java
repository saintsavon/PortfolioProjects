package SchoolProjects;

import java.util.Scanner;

public class EuclidDriver {

    public static void main(String[] args) {

        Scanner scan = new Scanner(System.in);
        System.out.println("Please enter first Positive integer.");
        int num1 = scan.nextInt();
        System.out.println("Please enter second Positive integer.");
        int num2 = scan.nextInt();
        System.out.println("The gcd of " + num1 + " and " + num2 + " is: " +  DivisorCal.gcd(num1, num2));

    }

}