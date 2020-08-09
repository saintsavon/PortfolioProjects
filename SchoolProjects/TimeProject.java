package SchoolProjects;

import java.util.Scanner;


public class TimeProject {
       public static void main(String[] args) {

              Scanner in = new Scanner(System.in);

              System.out.println("Input number of seconds:");

// Algorithm for calculating hours, minutes, and seconds from standard integer input.
              int input = in.nextInt();
              int hours = input / 60;
              int minutes = hours % 60;
              int seconds = input % 60;
              hours = hours / 60;

              System.out.println( hours + " Hour(s) " + minutes + " Minute(s) " + seconds + " Second(s) ");
       }
}