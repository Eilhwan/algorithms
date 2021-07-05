import java.lang.reflect.Array;
import java.util.ArrayList;

public class Strings {
    public String[] solution(String s)
    {
        int p = 0;
        int start = 0;

        ArrayList<String> answer = new ArrayList<>();
        ArrayList<String> answer1 = new ArrayList<>();
        for (int i = s.length() - 1; i >= 0; i--)
        {
            // abcxyxyabc
            p = s.indexOf(s.charAt(i));
            String temp = s.substring(start, p + 1);
            if (s.substring(p + 1, i  + 1).contains(temp))
            {
                answer.add(temp);
                answer1.add(0, temp);
                s = s.substring(p + 1, i - p);
                i = i - (p * 2) - 1;
            }
            else
            {
                answer.add(s);
                break;
            }
        }
        for (int i = 0; i < answer1.size(); i++)
        {
            answer.add(answer1.get(i));
        }
        String[] ans = answer.toArray(new String[answer.size()]);
        return ans;

    }

    public static void main(String[] args)
    {
        Strings sa = new Strings();
        String s = "abcxyqwertyxyabc";
        String[] a = sa.solution(s);
        for (String c: a)
        {
            System.out.println(a.toString());
        }

    }
}
