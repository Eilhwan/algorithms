package StructuralPatterns._07_bridge.After;

public class PoolParty implements Skin {
    private String name;

    public PoolParty(String name) {
        this.name = name;
    }

    @Override
    public String getName() {
        return this.name;
    }
}
