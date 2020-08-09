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

        while (ageGuess != age) {
        // sentinel value of correct age guess to terminate loop
            System.out.println("You guessed Wrong! Please guess again.");
            if (ageGuess > age)
                System.out.println("younger");
            else
                System.out.println("older");
                ageGuess = scan.nextInt();

            if (ageGuess == age) {
                System.out.println("Your guess of " + ageGuess + " years old is correct!");
            }
        }
    }
}