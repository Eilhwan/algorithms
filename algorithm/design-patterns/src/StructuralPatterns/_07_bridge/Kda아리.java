package StructuralPatterns._07_bridge;

public class Kda아리 implements Champion {

    @Override
    public void move() {
        System.out.println("kda아리 move");
    }

    @Override
    public void skillQ() {
        System.out.println("kda아리 Q");
    }

    @Override
    public void skillW() {
        System.out.println("kda아리 W");
    }

    @Override
    public void skillE() {
        System.out.println("kda아리 E");
    }

    @Override
    public void skillR() {
        System.out.println("kda아리 R");
    }
}
