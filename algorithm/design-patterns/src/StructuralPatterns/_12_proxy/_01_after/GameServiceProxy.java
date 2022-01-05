package StructuralPatterns._12_proxy._01_after;

public class GameServiceProxy implements GameService {

    private GameService gameService;

    public GameServiceProxy(GameService gameService) {
        this.gameService = gameService;
    }

    @Override
    public void startGame() {
        System.out.println("부여성 부여성 부여성~~");
        gameService.startGame();
        System.out.println("국내성 국내성 국내성~~");
    }
}
