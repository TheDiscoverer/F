import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;
import java.net.UnknownHostException;
import java.util.Scanner;
import javax.swing.*;

public class User {
	public static void main(String[] args) throws UnknownHostException, IOException{
		Socket client = new Socket("192.168.2.102",9956);
		String str =null;
		Scanner input = new Scanner(System.in);
		str=input.next();
		PrintWriter cc = new PrintWriter(client.getOutputStream());
		while(str != null){
			cc.write(str+"\n");		//ע���һ�����з�
			cc.flush();
			str=input.next();
		}
	}
}
