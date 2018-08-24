package ipnet;

import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.URLEncoder;
import java.util.Base64;

import com.fasterxml.jackson.databind.ObjectMapper;

public class Mycommand {
	
	
	
	

public static void main(String[] args) throws Exception {
	//测试例子
	
	   Mycommand command =new Mycommand();
	   String [] commandarr= {"LST ALMAF:SCSN=412011,ECSN=412011;","DSP BRD:srn=0,sn=15;","LST ALMAF:SCSN=412011,ECSN=412011;"};
	   command.excCommand("BADMME09BHW", commandarr);
}
	

	
	/***
	 * 
	 * @param device  网元
	 * @param command  指令
	 * @return
	 * @throws Exception
	 */
	
	public String excCommand(String device,String[] command) throws Exception  {
		
		
		
		 String user ="admin" ;
         String pwd = "`1qaz2wsx";
         String auth = user+":"+pwd;
         byte[] authby = auth.getBytes("UTF-8");
         String message = URLEncoder.encode("集中操作","utf-8");
         String authUser =Base64.getEncoder().encodeToString(authby);
		 StringBuilder path = new StringBuilder(); 
	      path.append("http://").append("10.216.6.231/WebApi/mml/").append(device).append("/").append(message); 
	      URL url = new URL(path.toString());
	  	  ObjectMapper mapper=new ObjectMapper();
	      String commandjs=mapper.writeValueAsString(command);

		HttpURLConnection  connection = (HttpURLConnection) url.openConnection();
        connection.setRequestMethod("POST");
        connection.setDoOutput(true);
        connection.setDoInput(true);
        connection.setConnectTimeout(10000);
        connection.setReadTimeout(10000);
        connection.setUseCaches(false);
        connection.setInstanceFollowRedirects(true);
        connection.setRequestProperty("Content-Type","application/json;charset=utf-8");
        connection.setRequestProperty("Authorization","Basic "+authUser);
        connection.connect();
        
        DataOutputStream out = new DataOutputStream(connection.getOutputStream());
        out.writeBytes(commandjs);
        out.flush();  

        StringBuffer buffer = new StringBuffer(""); 
        BufferedReader reader = new BufferedReader(new InputStreamReader(connection.getInputStream())); 
        String lines; 
        if(connection.getResponseCode()==200) {
   
        while ((lines = reader.readLine()) != null) { 
            lines = new String(lines.getBytes(), "utf-8"); 
            buffer.append(lines); 
          
        } 
        System.out.println(buffer); 
        
        }
        reader.close();
        out.close();
        connection.disconnect();
        return buffer.toString();
       
	
	}
	
	
}
	
	
	

	
		 
		
	
	 


	 
	

