import java.io.*;
import java.net.*;
import java.nio.charset.StandardCharsets;
import java.util.HashMap;
import java.util.Map;

public class KakaoApi {

    public static void main(String[] args) {
        String api_url = "https://kapi.kakao.com/v1/payment/ready";

        Map<String, String> requestHeaders = new HashMap<>();
        requestHeaders.put("Content-type", "application/x-www-form-urlencoded;charset=utf-8");
        requestHeaders.put("Authorization", "KakaoAK 4bd2b69c8dfa54f7fe6f24850431f46a");

        Map<String, String> requestBody = new HashMap<>();
        requestBody.put("cid", "TC0ONETIME");
        requestBody.put("partner_order_id", "partner_order_id");
        requestBody.put("partner_user_id", "partner_user_id");
        requestBody.put("item_name", "초코파이");
        requestBody.put("quantity", "1");
        requestBody.put("total_amount", "2200");
        requestBody.put("vat_amount", "200");
        requestBody.put("tax_free_amount", "0");
        requestBody.put("approval_url", "http://192.168.219.165/success");
        requestBody.put("fail_url", "http://192.168.219.165/fail");
        requestBody.put("cancel_url", "http://192.168.219.165/cancel");

        System.out.println(post(api_url, requestHeaders, requestBody));


    }

    private static String post(String api_url, Map<String, String> requestHeaders, Map<String, String> requestBody){
        HttpURLConnection con = connect(api_url);

        try {
            con.setRequestMethod("POST");
            for (Map.Entry<String, String> header : requestHeaders.entrySet()){
                con.setRequestProperty(header.getKey(), header.getValue());
            }
            StringBuffer params = new StringBuffer();
            for (Map.Entry<String, String> val: requestBody.entrySet()){
                params.append(val.getKey() + "=" + val.getValue() + "&");
            }
            System.out.println(params.toString());
            con.setDoOutput(true);
            con.getOutputStream().write(params.toString().getBytes());

            int responseCode = con.getResponseCode();
            if (responseCode == HttpURLConnection.HTTP_OK){
                return readBody(con.getInputStream());
            }else{
                return readBody(con.getErrorStream());
            }
        } catch (IOException e) {
            throw new RuntimeException("API 요청과 응답 실패");
        } finally {
            con.disconnect();
        }

    }

    private static HttpURLConnection connect(String api_url){
        try {
            URL url = new URL(api_url);
            return (HttpURLConnection)url.openConnection();
        } catch (MalformedURLException e){
            throw new RuntimeException("API URL이 잘못 되었습니다." + api_url, e);
        } catch (IOException e){
            throw new RuntimeException("연결이 실패되었습니다. :" +api_url, e);
        }
    }

    private static String readBody(InputStream body){
        InputStreamReader streamReader = new InputStreamReader(body);

        try(BufferedReader lineReader = new BufferedReader(streamReader)){
            StringBuilder responseBody = new StringBuilder();

            String line;
            while ((line = lineReader.readLine()) != null){
                responseBody.append(line);
            }

            return responseBody.toString();
        } catch (IOException e) {
            throw new RuntimeException("API응답을 읽는데 실패하였습니다.", e);
        }
    }
}
