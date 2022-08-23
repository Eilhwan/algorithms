package stream;

import java.util.Arrays;
import java.util.Iterator;
import java.util.List;
import java.util.stream.Stream;

public class StreamIterator {

    public static void main(String[] args) {
        List<String> l = Arrays.asList("홍길동", "백기선", "김자바", "김오동");

//        Iterator<String> iterator = l.iterator();
//
//        while (iterator.hasNext()) {
//            System.out.println(iterator.next());
//        }
        Stream<String> stream = l.stream();

//        stream.forEach( StreamIterator :: print);

        Stream<String> parallelStream = l.parallelStream();
        parallelStream.forEach(StreamIterator :: print);
    }

    private static void print(String s) {
        System.out.println(s + " : " + Thread.currentThread().getName());
    }


}
