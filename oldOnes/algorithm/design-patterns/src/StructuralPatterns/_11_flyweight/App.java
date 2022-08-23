package StructuralPatterns._11_flyweight;

public class App {
    public static void main(String[] args) {
        FontFactory fontFactory = new FontFactory();

        Character c1 = new Character('c', "blue", fontFactory.getFont("nanum:12"));
        Character c2 = new Character('a', "green", fontFactory.getFont("nanum:12"));
        Character c3 = new Character('d', "red", fontFactory.getFont("nanum:12"));
        Character c4 = new Character('o', "skyla", fontFactory.getFont("nanum:12"));
    }
}
