import java.util.*;
public class HelloWorld {

    public static void main(String[] args) {
                String pattern = "abbc";
                String str = "北京 杭州 杭州 北京";
                boolean has = wordPattern(pattern, str);
                System.out.println(has);
                System.out.println("Hello World");
                    
    }
    
    public static boolean wordPattern(String pattern, String str) {
            Map<Character, String> map = new HashMap<>();
            char[] ptArr = pattern.toCharArray();
            String[] strArr = str.split(" ");
            System.out.println(ptArr);
            System.out.println(strArr);
            if (ptArr.length != strArr.length) {
                return false;
            }
            for (int i = 0; i < ptArr.length; i++) {
                String val = map.get(ptArr[i]);
                if (null != val) {
                    return val.equals(strArr[i]);
                } else {
                    if (!map.values().contains(strArr[i])) {
                        map.put(ptArr[i], strArr[i]);
                        System.out.println(map);
                    } else {
                        return false;
                    }
                }
            }
            return true;
    }
}

