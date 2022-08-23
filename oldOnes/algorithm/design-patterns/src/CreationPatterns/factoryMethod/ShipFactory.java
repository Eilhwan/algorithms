package CreationPatterns.factoryMethod;

public interface ShipFactory {
    default Ship orderShip(String name, String email){
        validate(name, email);
        prefareFor(name);
        Ship ship = createShip();
        sendToEmail(email, ship);
        return ship;
    }

    private void sendToEmail(String email, Ship ship){
        System.out.println("To" + email + "\n" + ship.getName() + "다 만들었습니다.");
    };

    Ship createShip();

    private void validate(String name, String email){
        if (name == null && name.isBlank()) {
            throw new IllegalArgumentException("배 이름을 지어주세요.");
        }
        if (email == null && email.isBlank()) {
            throw new IllegalArgumentException("연락처를 남겨주세요.");
        }
    }

    private void prefareFor(String name){
        System.out.println(name + "배 만드는 중");
    }

}
