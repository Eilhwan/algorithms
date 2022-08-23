package CreationPatterns.factoryMethod2;

public class Client {

    public static void main(String[] args) {
        Car porsche = new Car();


        print(new BenzFactory(), "benz", "600HP", 10000000);

    }
    public static void print(CarFactory carFactory, String name, String engine, int price) {
        System.out.println(carFactory.orderCar(name, engine, price));
    }
}
