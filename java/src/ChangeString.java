public class ChangeString {
    public int solution(String s, String t)
    {
        int result = 0;
        while (true)
        {
            if (s.contains(t))
            {
                s = s.replace(t, "");
                result++;
            }
            else
            {
                break;
            }
        }
        return result;
    }

    public static void main(String[] args)
    {
        String s = "aabcbcd";
        String t = "abc";
        ChangeString c = new ChangeString();
        int r = c.solution(s, t);
        System.out.println(r);
    }
}
