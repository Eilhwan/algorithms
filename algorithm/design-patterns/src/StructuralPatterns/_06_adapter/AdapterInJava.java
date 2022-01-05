package StructuralPatterns._06_adapter;

import java.io.*;
import java.util.Arrays;
import java.util.Collections;
import java.util.Enumeration;
import java.util.List;

public class AdapterInJava {
    public static void main(String[] args) {
        // Collections
        List<String> a = Arrays.asList("a", "b", "c");
        Enumeration<String> b = Collections.enumeration(a);
        List<String> c = Collections.list(b);

        // io
        try(InputStream is = new FileInputStream(a.toString());
            InputStreamReader isr = new InputStreamReader(is);
            BufferedReader reader = new BufferedReader(isr)
        ) {
            while (reader.ready()) {
                System.out.println(reader.readLine());;
            }
        } catch (IOException e) {
            throw new RuntimeException();
        }
    }
}
