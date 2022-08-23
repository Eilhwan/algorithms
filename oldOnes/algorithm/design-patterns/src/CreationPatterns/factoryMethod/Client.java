package CreationPatterns.factoryMethod;

public class Client {
    public static void main(String[] args) throws Exception {
        Client client = new Client();
        client.print(new WhiteShipFactory(), "Keesun", "keesun@gmail.com");
        client.print(new BlackShipFactory(), "Keesun2", "keesun@gmail.com");


    }

    public void print(ShipFactory shipFactory, String name, String email){
        System.out.println(shipFactory.orderShip(name, email));
    }
}
