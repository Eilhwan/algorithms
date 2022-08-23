package dataStructures;

import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.Stack;

public class Arrays {

    public static void main(String[] args) {
        Stack<Integer[]> st = new Stack<>();
        int[] v = {1, 2};
        st.add(java.util.Arrays.stream(v).boxed().toArray(Integer[]::new));
        ArrayList<Integer> i = new ArrayList<>();
        Collections.sort(i);
        java.util.Arrays.stream(v).boxed().toArray(String[]::new);


    }
}
