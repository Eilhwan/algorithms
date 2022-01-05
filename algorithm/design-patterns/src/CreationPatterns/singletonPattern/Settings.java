package CreationPatterns.singletonPattern;

import java.io.Serializable;
import java.lang.reflect.Constructor;

public class Settings implements Serializable {

    private Settings() {}

    private static class SettingsHolder{
        private static final Settings INSTANCE = new Settings();
    }

    public static Settings getInstance(){
        return SettingsHolder.INSTANCE;
    }

    public static void main(String[] args) throws Exception{
        Settings s1 = Settings.getInstance();
        Constructor<Settings> constructor = Settings.class.getDeclaredConstructor();
        constructor.setAccessible(true);
        Settings s2 = constructor.newInstance();
        System.out.println(s1 == s2);
//        Runtime runtime = new Runtime();
        Setting s3 = Setting.INSTANCE;
        System.out.println(s3.name().equals("INSTANCE"));
    }
}
