package StructuralPatterns._11_flyweight;

import java.util.HashMap;

public class FontFactory {
    HashMap<String, Font> cache = new HashMap<>();

    public FontFactory() {
    }

    public Font getFont(String font) {

        if (cache.containsKey(font)) {
            return cache.get(font);
        } else {
            String[] split = font.split(":");
            Font newFont =
            new Font(split[0],Integer.parseInt(split[1]));
            cache.put(font, newFont);
            return newFont;
        }

    }
}
