import java.io.BufferedReader;
import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.InetAddress;
import java.net.ServerSocket;
import java.net.Socket;
import java.sql.Time;
import java.util.Scanner;
import javax.print.attribute.standard.Severity;
import javax.sound.midi.Receiver;
class order {
	ServerSocket PiserverSocket = null;
	ServerSocket UserServerSocket=null;
	ServerSocket ssSocket=null;
	Socket UserSocket=null,PiSocket=null;
	public order() throws IOException{
		PiserverSocket = new ServerSocket(9955); // 创建树莓派端服务器socket
		UserServerSocket=new ServerSocket(9956);// 创建用户端服务器socket
		ssSocket = new ServerSocket(9960);		//创建接受图片的服务器socket
		InetAddress address = InetAddress.getLocalHost();
		String hoString=address.getHostAddress();
		System.out.println(hoString);
		PiSocket = PiserverSocket.accept();  //创建树莓派连接的socket
		System.out.println("S connect from:" + PiSocket.getInetAddress().getHostAddress());
		
		while(true){
		
			UserSocket = UserServerSocket.accept();
			System.out.println("S connect from:" + UserSocket.getInetAddress().getHostAddress());
			/*if(PiSocket == null){
				PiSocket = PiserverSocket.accept();  //创建树莓派连接的socket
				System.out.println("S connect from:" + PiSocket.getInetAddress().getHostAddress());
			}*/
			Receive receive = new Receive(UserSocket,PiSocket,ssSocket);
			receive.start();
			//new ReceivePic().start();
		}
	}
}
/*
class ReceivePic extends Thread{
	ServerSocket pSocket = new ServerSocket(9961);
	public ReceivePic() throws IOException{	
	}
	public void run(){
		Socket fsocket=null;
		while(true){
			try {
				fsocket = pSocket.accept();
			} catch (IOException e) {
			}
			new fileReceive(fsocket).start();
		}
	}
}
*/

class Receive extends Thread{
	String ReceiveString =null;
	Socket UserSocket=null;
	Socket PiSocket =null;
	ServerSocket ssSocket = null;
	PrintWriter pw=null;
	public boolean exit=true;
	public Receive(Socket UserSocket,Socket PiSocket,ServerSocket ssSocket2) throws IOException{
		this.UserSocket=UserSocket;
		this.PiSocket=PiSocket;
		this.ssSocket = ssSocket2;	
	}
	public void run(){
		try {
			BufferedReader breader = new BufferedReader(new InputStreamReader(UserSocket.getInputStream()) );
			pw = new PrintWriter(PiSocket.getOutputStream(), true);
			ReceiveString = breader.readLine();
			
			while(exit){
				if(ReceiveString!=null){
					System.out.println(ReceiveString);
					pw.println(ReceiveString); 
					System.out.println(ReceiveString.substring(0,6));
					if(ReceiveString.equals("getPicture"))
					{
						Socket fsocket =ssSocket.accept();
						new fileReceive(fsocket).start();
					}
					
					if(ReceiveString.substring(0,6).equals("zhuan|"))
					{
						
							Socket fsocket =ssSocket.accept();
							new fileReceive(fsocket).start();						
					}
					ReceiveString=null;
					ReceiveString = breader.readLine();
				}
			}
		}catch (IOException e){
			exit=false;
		}
	}
}

class fileReceive extends Thread {
    Socket s;
    public fileReceive(Socket s) {
        this.s = s;
    }
    @Override
    public void run() {
        System.out.println("in handling..");
        FileOutputStream fos = null;
        try {
            InputStream is = s.getInputStream();
            BufferedReader in = new BufferedReader(new InputStreamReader(is));
            // 从客户端读取发送过来的文件名
            String filename = in.readLine();
            System.out.println(filename);
            File file = new File("E:\\xampp\\htdocs\\test\\pic",filename);
            int len = 0;
            int BUFSIZE = 4*1024;
            byte[] by = new byte[BUFSIZE * 1024];
            fos = new FileOutputStream(file);
            while ((len = is.read(by, 0, BUFSIZE)) != -1) {
                fos.write(by,0,len);
                fos.flush();
            }
            System.out.println("done.");   
        }catch (Exception e) {
            e.printStackTrace();
        }finally {
            //服务端就不要手贱 关了socket否则Python 会出现错误Errno 10054让客户端关掉就行啦
            try {
                fos.close();
            }catch (IOException e) {
                e.printStackTrace ();
            }
        }
    }
}
public class Server{
	public static void main(String[] args) throws IOException {
		System.out.println("wait for connect......");
		new order();
	}
}