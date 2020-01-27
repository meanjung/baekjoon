package 자료구조;
import java.util.*;
public class java13413 {

	public static void main(String[] args) {
		Scanner kbd=new Scanner(System.in);
		int T=kbd.nextInt();
		int N[]=new int[T];
		int res[]=new int[T];
		String str1=new String();
		String str2=new String();
		for(int i=0;i<T;i++) {
			N[i]=kbd.nextInt();
			str1=kbd.next();
			str2=kbd.next();
			res[i]=solve(str1,str2);
		}
		for(int i=0;i<T;i++)
			System.out.println(res[i]);

	}
	static int solve(String str1,String str2) {
		int W1=0;
		int B1=0;
		int W2=0;
		int B2=0;
		for(int i=0;i<str1.length();i++) {
			if(str1.charAt(i)!=str2.charAt(i)) {
				if(str1.charAt(i)=='W')
					W1++;
				else if(str1.charAt(i)=='B')
					B1++;
			}
		}
		W2=B1;
		B2=W1;
		if(W1==0)
			return B1;
		else if(B1==0)
			return W1;
		else return Math.min(W1,B1)+Math.abs(W1-B1);
		
	}

}
