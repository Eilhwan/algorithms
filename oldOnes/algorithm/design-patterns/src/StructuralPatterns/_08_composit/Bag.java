package StructuralPatterns._08_composit;

import java.util.ArrayList;
import java.util.List;

public class Bag {

    private List<Item> items;

    public List<Item> getItems() {
        return items;
    }

    public void add(Item item) {
        if (this.items == null) {
            items = new ArrayList<>();
        }
        items.add(item);
    }
}
