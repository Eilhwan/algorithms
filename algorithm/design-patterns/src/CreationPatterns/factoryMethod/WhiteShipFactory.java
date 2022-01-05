package CreationPatterns.factoryMethod;

public class WhiteShipFactory implements ShipFactory{

    @Override
    public Ship createShip() {
        Ship ship = new WhiteShip();
        return ship;
    }
}
