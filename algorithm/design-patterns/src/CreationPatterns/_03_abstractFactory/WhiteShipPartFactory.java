package CreationPatterns._03_abstractFactory;

public class WhiteShipPartFactory implements ShipPartFactory {

    @Override
    public Anchor createAnchor() {
        return new WhiteShipAnchor();
    }

    @Override
    public Wheel createWheel() {
        return new WhiteShipWheel();
    }
}
