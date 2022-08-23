package CreationPatterns.factoryMethod2;

public interface CarFactory {
    default Car orderCar(String name, String engine, int price){
        validate(name, engine);
        System.out.println(name + "is being made by Apple in California!");
        Car car = createCar(name, engine, price);
        System.out.println(car.getName() + "'s building complete");

        return car;

    }

    Car createCar(String name, String engine, int price);

    private void validate(String name, String engine){
        if (name == null || name.isBlank()) {
            throw new IllegalArgumentException("There is no name!");
        }
        if (engine == null || engine.isBlank()) {
            throw new IllegalArgumentException("There is no name!");
        }
    };


}
