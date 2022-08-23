package StructuralPatterns._12_proxy._01_after;

public class DefaultGameService implements GameService {

    @Override
    public void startGame() {
        System.out.println("바람의 나라 바람의 나라~~");
    }
}
