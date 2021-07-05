import java.util.Queue;
import java.util.Stack;

public class DeletePair {

    public int solution(String s)
    {
        Stack<Character> st = new Stack<Character>();

        for (int i = 0; i < s.length(); i++)
        {
            if (st.size() > 0)
            {
                char temp = st.pop();
                if (s.charAt(i) != temp)
                {
                    st.add(temp);
                    st.add(s.charAt(i));
                }
            }
            else
            {
                st.add(s.charAt(i));
            }
        }
        if (st.size() > 0) return 1;
        else return 0;
    }

    public static void main(String[] args)
    {
        DeletePair d = new DeletePair();
        System.out.println(d.solution("baabaa"));

    }
}
