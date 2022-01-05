package StructuralPatterns._08_composit.after;

import java.util.ArrayList;
import java.util.List;

public class Bag implements Component {

    private List<Component> components;

    public List<Component> getComponents() {
        return components;
    }

    public void add(Component component) {
        if (this.components == null) {
            components = new ArrayList<>();
        }
        components.add(component);
    }

    @Override
    public int getPrice() {
        return this.getComponents().stream().mapToInt(Component::getPrice).sum();
    }
}
