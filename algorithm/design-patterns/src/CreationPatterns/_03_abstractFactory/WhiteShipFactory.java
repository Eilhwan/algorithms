package CreationPatterns._03_abstractFactory;

import CreationPatterns.factoryMethod.Ship;
import CreationPatterns.factoryMethod.ShipFactory;
import CreationPatterns.factoryMethod.WhiteShip;

public class WhiteShipFactory implements ShipFactory {

    private ShipPartFactory shipPartFactory;

    public WhiteShipFactory(ShipPartFactory shipPartFactory){
        this.shipPartFactory = shipPartFactory;
    }

    @Override
    public Ship createShip() {
        Ship ship = new WhiteShip();
        ship.setWheel(shipPartFactory.createWheel());
        ship.setAnchor(shipPartFactory.createAnchor());

        return ship;
    }
}
