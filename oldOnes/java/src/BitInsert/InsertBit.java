package BitInsert;

public class InsertBit {
    int Insert_Bit(int n, int m, int i, int j, boolean front)
    {
        // n의 j부터 i까지의 비트를 0으로 변환한다.
        // m을 시프트 하여서 j부터 i까지 오도록 한다.
        // m과 n을 합한다.
        int allOnes = ~0;
        int left = allOnes << (j + 1);
        int right = ((1 << i) - 1);
        int mask = left | right;
        int m_shifted = 0;
        int length = j + i - Integer.toBinaryString(m).length();
        int n_cleared = n & mask;
        System.out.println(length);
        if (front)
            m_shifted = m << length;
        else
            m_shifted = m << i;

        return n_cleared | m_shifted;
    }
    public static void main(String[] args)
    {
        int n = 0b1000000000;
        int m = 0b10011;

        int i = 2;
        int j = 7;

        InsertBit io = new InsertBit();
        int res = io.Insert_Bit(n, m, i, j, true);
        System.out.println(Integer.toBinaryString(res));
    }
}
