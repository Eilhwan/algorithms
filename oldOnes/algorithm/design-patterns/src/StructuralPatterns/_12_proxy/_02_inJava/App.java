package StructuralPatterns._12_proxy._02_inJava;

import StructuralPatterns._12_proxy._01_after.DefaultGameService;
import StructuralPatterns._12_proxy._01_after.GameService;
import StructuralPatterns._12_proxy._01_after.GameServiceProxy;

import java.lang.reflect.InvocationHandler;
import java.lang.reflect.Method;
import java.lang.reflect.Proxy;

public class App {
    public static void main(String[] args) {

    }

    public void dynamicProxy() {
        GameService gameServiceProxy = new GameServiceProxy(new DefaultGameService());
        gameServiceProxy.startGame();
    }

    private GameService getGameServiceProxy(GameService target) {
        return (GameService) Proxy.newProxyInstance(this.getClass().getClassLoader(),
                new Class[]{GameService.class}, new InvocationHandler() {
                    @Override
                    public Object invoke(Object proxy, Method method, Object[] args) throws Throwable {
                        System.out.println("Hi");
                        method.invoke(target, args);
                        System.out.println("bye");
                        return null;
                    }
                }
        );
    }
}
