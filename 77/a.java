import java.net.URLDecoder;
import java.util.*;

class A {
    public static void main(String args[]) {
        String a = "HelloWolrd!!!";
        byte[] ba = a.getBytes();
        for (int i = 0; i < ba.length; i++) {
            System.out.print(ba[i] + " ");
           }
        // System.out.println(a + a.getBytes());
        String urlEncoded = urlEncode(a.getBytes());
        System.out.println("");
        System.out.println(urlEncoded);
        String base64Encoded = base64Encode(urlEncoded.getBytes());
        System.out.println(base64Encoded);
    }
    public static String base64Encode(byte[] input) {
        return Base64.getEncoder().encodeToString(input);
    }
    public static String urlEncode(byte[] input) {
        StringBuffer buf = new StringBuffer();
        for (int i=0; i<input.length; i++) {
            buf.append(String.format("%%%2x", input[i]));
            buf.append("");
        }
        return buf.toString();
    }
}
