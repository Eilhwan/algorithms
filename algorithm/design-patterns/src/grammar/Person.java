package grammar;

public class Person {
    private int order;

    public int getOrder() {
        return order;
    }

    public void setOrder(int order) {
        this.order = order;
    }

    @Override
    public String toString() {
        return "Person{" +
                "order=" + order +
                '}';
    }
}
