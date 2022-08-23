package CreationPatterns.factoryMethod2;

public class BenzFactory implements CarFactory {
    @Override
    public Car createCar(String name, String engine, int price) {
        Car benz = new Car();

        benz.setName(name);
        benz.setEngine(engine);
        benz.setPrice(price);

        return benz;
    }
}
