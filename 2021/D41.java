import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class D41 {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new FileReader("d4e.txt"));
        String line = reader.readLine().trim();
        String[] seq = line.split(",");
        
        int c = 0;
        String[][] board = new String[5][5];
        while(line != null) {
            if (line.equals("")) {
                c+=1;
                
            }
        }
        System.out.println(c);
        reader.close();
    }

}