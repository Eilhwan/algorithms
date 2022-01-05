package CreationPatterns._03_abstractFactory;

public interface ShipPartFactory {
    Anchor createAnchor();

    Wheel createWheel();
}
