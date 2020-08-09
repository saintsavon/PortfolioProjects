package SchoolProjects;

import java.util.Scanner;

public class VowelCounter {
    public static void main(String[] args) {

        Scanner scan = new Scanner(System.in);
        String UserInput;

        System.out.println("Please type in a phrase consisting solely of letters.");

        UserInput = scan.nextLine();
        int vowels = 0, consonants = 0, a = 0, e = 0, i = 0, o = 0, u = 0;

        for(int x = 0; x < UserInput.length(); ++x) {

            char ch = UserInput.charAt(x);

            if(ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u') {
                ++vowels;
              } 
            else if(ch >= 'a'&& ch <= 'z') {
              ++consonants;
              }
            if(ch == 'a') {
                ++a;
              }
            if(ch == 'e') {
                ++e;
              }
            if(ch == 'i') {
                ++i;
              }
            if(ch == 'o') {
                ++o;
              }
            if(ch == 'u') {
                ++u;
              }
        }
              System.out.println("Vowels = " + vowels);
              System.out.println("Consonants = " + consonants);
              System.out.println("a's = " +a);
              System.out.println("e's = " +e);
              System.out.println("i's = " +i);
              System.out.println("o's = " +o);
              System.out.println("u's = " +u);
    }
}

