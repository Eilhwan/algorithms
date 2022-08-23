package designPattern.singleton;

public class EagerSingleton {
    private static EagerSingleton instance = new EagerSingleton();

    private EagerSingleton(){}

    public static EagerSingleton getInstance(){
        return instance;
    }
    
    public static void main(String[] args) {
        EagerSingleton instance = EagerSingleton.getInstance();
        EagerSingleton instance2 = EagerSingleton.getInstance();

        System.out.println(instance.hashCode());
        System.out.println(instance2.hashCode());
        Thread[] threads = new Thread[10];
        for (int ii = 0; ii < threads.length; ii++)
        {
            Thread thread = new Thread(() -> {
                EagerSingleton i = EagerSingleton.getInstance();
            });
            threads[ii] = thread;
        }

        for (Thread t:
                threads) {
            t.run();
            System.out.println(t);
        }
    }

}
