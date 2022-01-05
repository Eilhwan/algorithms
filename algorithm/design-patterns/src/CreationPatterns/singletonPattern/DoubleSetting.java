package CreationPatterns.singletonPattern;

public class DoubleSetting {
    private static volatile DoubleSetting instance;

    private DoubleSetting() {}

    public static DoubleSetting getInstance(){
        if (instance == null) {
            synchronized (DoubleSetting.class) {
                if (instance == null) {
                    instance = new DoubleSetting();
                }
            }
        }
        return instance;
    }
}
