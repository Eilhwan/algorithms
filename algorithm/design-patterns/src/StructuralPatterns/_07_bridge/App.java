package StructuralPatterns._07_bridge;

import StructuralPatterns._07_bridge.After.KDA;
import StructuralPatterns._07_bridge.After.PoolParty;
import StructuralPatterns._07_bridge.After.Skin;
import StructuralPatterns._07_bridge.After.아리;

public class App {
    public static void main(String[] args) {
        // Champion - abstraction
        // KDA스킨 - concrete Impl

        Champion kda아리 = new 아리(new KDA());

        kda아리.move();
        kda아리.skillQ();

        Champion poolParty아리 = new 아리(new PoolParty("풀파티 지건"));
        poolParty아리.move();

    }
}
