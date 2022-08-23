package StructuralPatterns._08_composit.after;


import javax.swing.*;

public class Client {
    public static void main(String[] args) {
        Item doranBlade = new Item("도란검", 450);
        Item healPortion = new Item("체력 물약", 50);

        Bag bag = new Bag();
        bag.add(doranBlade);
        bag.add(healPortion);

        Client client = new Client();

        client.printPrice(doranBlade);
        client.printPrice(bag);
        JFrame jFrame = new JFrame();
        jFrame.setSize(400, 400);
        jFrame.add(new JButton("Hello world"));
        jFrame.setVisible(true);
    }

    private void printPrice(Component component) {
        System.out.println(component.getPrice());
    }
}
