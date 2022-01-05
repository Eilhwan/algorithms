package StructuralPatterns._12_proxy._01_after;

public class App {

    public static void main(String[] args) {
        GameService gs = new GameServiceProxy(new DefaultGameService());

        gs.startGame();
    }
}
