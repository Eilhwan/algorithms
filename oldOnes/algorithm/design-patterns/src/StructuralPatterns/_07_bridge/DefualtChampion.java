package StructuralPatterns._07_bridge;

import StructuralPatterns._07_bridge.After.Skin;

public class DefualtChampion implements Champion {

    private Skin skin;

    public DefualtChampion(Skin skin, String name) {
        this.skin = skin;
        this.name = name;
    }

    private String name;
    @Override
    public void move() {
        System.out.println(skin.getName() + name + "move!");
    }

    @Override
    public void skillQ() {
        System.out.println(skin.getName() + name + "Q");
    }

    @Override
    public void skillW() {

    }

    @Override
    public void skillE() {

    }

    @Override
    public void skillR() {

    }
}
