import java.util.Arrays;
import java.util.Collection;
import java.util.Collections;
import java.util.Comparator;

public class Coupon {
    public int solution(int[] prices, int[] discounts) {
        int answer = 0;
        Integer[] price = Arrays.stream(prices).boxed().toArray(Integer[]::new);
        Integer[] discount = Arrays.stream(discounts).boxed().toArray(Integer[]::new);

        Arrays.sort(price, Collections.reverseOrder());
        Arrays.sort(discount, Collections.reverseOrder());
        int i;
        for (i = 0; i < discounts.length; i++)
        {
            answer += prices[i] * ((double)discounts[i] / 100);
        }
        for (int j = i + 1; j < prices.length; j++)
        {
            answer += prices[j];
        }
        System.out.println(answer);
        return answer;
    }

    public static void main(String[] args) {
        int[] prices = {13000, 88000, 10000};
        int[] discounts = {30, 20};
        Coupon c = new Coupon();
        c.solution(prices, discounts);
    }
}
