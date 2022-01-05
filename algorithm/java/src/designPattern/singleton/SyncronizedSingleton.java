package designPattern.singleton;

public class SyncronizedSingleton {
    private static SyncronizedSingleton instance;

    private SyncronizedSingleton(){}

    public synchronized static SyncronizedSingleton getInstance(){
        if (instance == null){
            instance =  new SyncronizedSingleton();
            return instance;
        }
        return instance;
    }
}
