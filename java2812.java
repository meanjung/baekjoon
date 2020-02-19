package 자료구조;
import java.util.*;
public class java2812 {

	public static void main(String[] args) {
		Scanner kbd=new Scanner(System.in);
		int n=kbd.nextInt();
		int k=kbd.nextInt();
		int t=0;
		char c;
		char s[]=new char[n];
		String str=kbd.next();
		while(n-->0) {
			do {
				c=str.charAt(str.length()-n-1);
			}while(c<48||57<c);
			while(k>0&&t>0&&s[t-1]<c) {
				t--;
				k--;
			}
			s[t++]=c;
		}
		t-=k;
		for(k=0;k<t;k++)
			System.out.println(s[k]);
	}

}
