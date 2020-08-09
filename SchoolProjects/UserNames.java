package SchoolProjects;

import java.util.Scanner;
import java.util.Random;

public class UserNames {
    public static void main(String[] args) {

        String FirstName, LastName;
        String mutation1, mutation2;
        int number;
        Scanner scan = new Scanner (System.in);

        System.out.println("What is your first name?");

        FirstName = scan.nextLine();
        mutation1 = FirstName.substring(0,1);

        System.out.println("What is your last name?");

        LastName = scan.nextLine();
        mutation2 = LastName.substring(0,4);

        Random gen = new Random();
        int randnum = 10 + gen.nextInt(109);

        number = randnum;

        System.out.println( mutation2 + mutation1 + number);
       }
}