package SchoolProjects;

import java.io.*;

public class FileCreator {

    public static void main(String[] args) throws IOException {

        String str;
        BufferedReader br = new BufferedReader (new InputStreamReader(System.in));
        BufferedWriter bout = new BufferedWriter (new FileWriter("userStrings.txt"));
        System.out.println("Enter String (Type 'DONE' to end)");
        int i=1;

        while (i>0)

        {

        str = br.readLine();

        if (str.contentEquals("DONE")) {
        break;
        }
        else {
        i++;
        }
        
        bout.write(str);
        bout.newLine();
        }
        bout.close();
    }

}