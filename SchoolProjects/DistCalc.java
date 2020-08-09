package SchoolProjects;

import java.util.Scanner;
import java.text.DecimalFormat;
import java.util.Random;

public class DistCalc {
    public static void main(String[] args) {

        String coordinates;

        double x1, x2, y1, y2, discriminant, dist;

        Scanner scan = new Scanner(System.in);

        System.out.println("Input your x1 coordinate:");
        x1 = scan.nextInt();
        System.out.println("Input your x2 coordinate:");
        x2 = scan.nextInt();
        System.out.println("Input your y1 coordinate:");
        y1 = scan.nextInt();
        System.out.println("Input your y2 coordinate:");
        y2 = scan.nextInt();

        discriminant = (Math.pow(x2 - x1, 2)) + (Math.pow(y2 - y1, 2));
        dist = Math.sqrt(discriminant);

        // Rounds the output to 3 decimal places
        DecimalFormat fmt = new DecimalFormat ("0.###");       

        System.out.println("Distance = "  + fmt.format(dist) + ".");
       }

}