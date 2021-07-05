public class NormalSquares {
    public long getGcd(int w, int h)
    {
        while(h != 0)
        {
            int temp = w % h;
            w = h;
            h = temp;
        }
        return Math.abs(w);
    }

    public long Solution(int w, int h)
    {
        return w * h - (w * h -  getGcd(w, h));
    }

}
