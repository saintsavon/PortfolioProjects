package SchoolProjects;

import java.util.Scanner;
import java.util.Random;

public class AgeGuess {
    public static void main(String[] args) {

        String username;
        int ageGuess;
        int birthyear;
        int age;

        Scanner scan = new Scanner (System.in);
        Random gen = new Random();

        int randnum = gen.nextInt(100);

        System.out.println("What is your first name?"); username = scan.nextLine();
        System.out.println("Hello " + username + ", what is your age guess?");

        ageGuess = scan.nextInt();
        age = randnum;

        System.out.println("Your guess is " + ageGuess + " years old. The correct answer was " + age +".");
       }
}