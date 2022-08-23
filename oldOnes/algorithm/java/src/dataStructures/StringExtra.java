package dataStructures;

import java.util.ArrayList;
import java.util.Stack;

public class StringExtra {
    public static void main(String[] args) {
        String s = "abccdcba";

        // palindrome
        boolean is_pen = true;
        for (int i = 0; i < s.length() / 2; i++)
        {
            if (s.charAt(i) != (s.charAt(s.length() - 1 - i)))
                is_pen = false;
        }

//        System.out.println(is_pen ? "This is a palindrome" : "This is not palindrome");

        // split
        class Product {
            String name;
            int value;
            Product(String name, int value){
                this.name = name;
                this.value = value;
            }
        }
        String s1 = "kimchi: 1000, fish: 10000, meat: 1200, sauce: 300";
        // -> list
        String[] goods = s1.split(",");
        Product[] products = new Product[goods.length];
        int index = 0;
        for (String good : goods){
            String[] temp = good.split(":");
            Product p = new Product(temp[0].trim(), Integer.parseInt(temp[1].trim()));
            products[index] = p;
            index++;
        }

        for (Product p : products)
            System.out.println(p.name + " : " + p.value);

        Stack<Integer> st = new Stack<>();

    }
}
