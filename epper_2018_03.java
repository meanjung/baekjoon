package 자료구조;
import java.util.*;
public class epper_2018_03 {

	public static void main(String[] args) {
		Scanner kbd=new Scanner(System.in);
		String str=new String();
		str=kbd.next();
		char result[]=new char[str.length()];
		int j=1;
		result[0]=str.charAt(0);
		for(int i=1;i<str.length();i++) {
			if(str.charAt(i)=='-')
				result[j++]=str.charAt(i+1);
		}
		for(int k=0;k<j;k++)
			System.out.print(result[k]);
	}

}
