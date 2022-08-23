package CreationPatterns.singletonPattern;

public class singleton1 {
    private static singleton1 instance;
    private singleton1 (){}

    public static singleton1 getInstance() {
        if (instance == null) {
            instance = new singleton1();
        }
        return instance;
    }
}
