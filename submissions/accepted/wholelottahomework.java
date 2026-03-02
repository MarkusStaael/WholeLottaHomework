import java.io.BufferedReader;
import java.io.InputStreamReader;

public class wholelottahomework {

    public static void main(String[] args) throws Exception {

        BufferedReader r = new BufferedReader(new InputStreamReader(System.in));

        int nlines = Integer.parseInt(r.readLine());

        for(int i = 0; i < nlines; i++) {

            String[] str = r.readLine().split(" "); 

            switch(str[1]) {
                case "+":
                    System.out.println(Integer.parseInt(str[0]) + Integer.parseInt(str[2]));
                    break;
                case "-":
                    System.out.println(Integer.parseInt(str[0]) - Integer.parseInt(str[2]));
                    break;
            }
        }
    }
}