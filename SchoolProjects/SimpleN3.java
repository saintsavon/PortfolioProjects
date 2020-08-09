package SchoolProjects;

import java.util.Scanner;

public class SimpleN3 {

    public static void main(String[] args) {

        int N,result1;
        System.out.print("Enter the number : ");
        Scanner scan = new Scanner(System.in);
        N = scan.nextInt();
        result1 = Othree(N);
        System.out.println(result1);
    }

    public static int Othree(int N) {

        int result = 0;
        for(int i = 0;i < N; i++) // Its complexity is O(n)
        for(int j= 0 ; j < N; j++) // Its complexity is O(n2)
        for(int k = 0; k <N; k++) // Its complexity is O(n3)
        result++; // Its complexity is O(n3)
        return result; // return result

    }

}