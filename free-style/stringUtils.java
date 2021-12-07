public class stringUtils {
    public static String defaultIfEmpty(Object value, String defaultValue) {
	    return value == null ? defaultValue : (String) value;
	}
	
    public static void main(String[] args) {
        System.out.println( defaultIfEmpty(1, ""));
        System.out.println( defaultIfEmpty("aaa", ""));
        System.out.println( defaultIfEmpty(133.4, ""));
       
    }
}
