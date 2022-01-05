package CreationPatterns._03_abstractFactory;

public class WhiteShipProPartFactory implements ShipPartFactory{

    @Override
    public Anchor createAnchor() {
        return new WhiteShipProAnchor();
    }

    @Override
    public Wheel createWheel() {
        return new WhiteShipProWheel();
    }
}
