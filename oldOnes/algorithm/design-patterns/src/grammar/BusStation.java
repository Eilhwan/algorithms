package grammar;

import java.util.Queue;

public class BusStation {

    private Queue<Person> people;

    public void setQueue(Person person) {
        this.people.add(person);
    }

    @Override
    public String toString() {
        return "BusStation{" +
                "people=" + people +
                '}';
    }
}
