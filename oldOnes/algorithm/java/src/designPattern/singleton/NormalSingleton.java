package designPattern.singleton;

public class NormalSingleton {

    private static NormalSingleton instance;

    private NormalSingleton(){}

    public static NormalSingleton getInstance(){
        if (instance == null){
            instance =  new NormalSingleton();
            return instance;
        }
        return instance;
    }

    public static void main(String[] args) {
        NormalSingleton instance = NormalSingleton.getInstance();
        NormalSingleton instance2 = NormalSingleton.getInstance();

        System.out.println(instance.hashCode());
        System.out.println(instance2.hashCode());
        Thread[] threads = new Thread[10];
        for (int ii = 0; ii < threads.length; ii++)
        {
            Thread thread = new Thread(() -> {
                NormalSingleton i = NormalSingleton.getInstance();
            });
            threads[ii] = thread;
        }

        for (Thread t:
             threads) {
            System.out.println(t.hashCode());
        }
    }
}
