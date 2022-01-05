package dobulecolon;

import java.util.Arrays;
import java.util.Comparator;

public class LambdaColon {
    private  String name;
    private Integer value;

    public LambdaColon(String name, Integer value) {
        this.name = name;
        this.value = value;
    }

    public LambdaColon(Integer value) {
        this.value = value;
    }

    public Integer getValue() {
        return value;
    }

    public String getName() {
        return name;
    }

    public static void main(String[] args) {

        String name1 = "Vin";
        String name2 = "Scott";

        Integer value1 = 160;
        Integer value2 = 150;

        LambdaColon s1 = new LambdaColon(name1, value1);
        LambdaColon s2 = new LambdaColon(name2, value2);

        Comparator<LambdaColon> c1 = new Comparator<LambdaColon>() {
            @Override
            public int compare(LambdaColon o1, LambdaColon o2) {
                return o1.getValue() - o2.getValue();
            }
        };

//        System.out.println(c1.compare(s1, s2));
        Comparator<LambdaColon> c2 = (LambdaColon o1, LambdaColon o2) -> o1.getValue().compareTo(o2.getValue());
        System.out.println(c2.compare(s1, s2));

        Comparator<LambdaColon> c3 = Comparator.comparing(LambdaColon::getValue);
        System.out.println(c3.compare(s1, s2));

        int[] intArray = {1, 2, 3, 4, 5};

        Integer[] integers = Arrays.stream(intArray).boxed().toArray(Integer[]::new);
        Arrays.stream(integers).forEach(System.out::println);
        int a = 1;
//        Comparator.reverseOrder()
    }

}
