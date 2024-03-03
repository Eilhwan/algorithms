import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
// N-Queen
public class Main {
	public static int[] arr;
    public static int answer = 0;
    
    public static boolean check(int row) {
        for(int i = 0; i < row; i++) {
            if(arr[i] == arr[row] || row - i == Math.abs(arr[row] - arr[i])) {
                return false;
            }
        }
        return true;
    }
               
    public static void recursive(int row) {
        if(row == arr.length) {
            Main.answer += 1;
            return ;
        }
        
        for(int i = 0; i < arr.length; i++) {
            arr[row] = i;
            if(Main.check(i)) {
                recursive(row+1);
            }
        }
    }
    
    
	public static void main(String[] args) throws IOException {
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(in.readLine());
		
		arr = new int[N];
        Main.recursive(0);
        System.out.println(answer);
		
	}
	
}