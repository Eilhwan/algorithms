package CreationPatterns._03_abstractFactory;

import CreationPatterns.factoryMethod.Ship;
import CreationPatterns.factoryMethod.ShipFactory;

public class ShipInventory {
    public static void main(String[] args) {
        ShipFactory shipFactory = new WhiteShipFactory(new WhiteShipProPartFactory());
        Ship ship = shipFactory.createShip();
        System.out.println(ship.getAnchor().getClass());
        System.out.println(ship.getWheel().getClass());
    }
}
