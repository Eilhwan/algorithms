package designPattern.singleton;

public class InnerStaticSingleton {

    private InnerStaticSingleton(){}

    private static class LazySingletonHolder{
        private static final InnerStaticSingleton INSTANCE = new InnerStaticSingleton();
    }
    public static InnerStaticSingleton getInstance(){
        return LazySingletonHolder.INSTANCE;
    }
}
