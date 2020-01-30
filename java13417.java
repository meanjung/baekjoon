package 자료구조;
import java.util.*;
public class java13417 {

	public static void main(String[] args) {
		Scanner kbd=new Scanner(System.in);
		int T=kbd.nextInt();
		String res[]=new String[T];
		for(int i=0;i<T;i++) {
			int N=kbd.nextInt();
			String list[]=new String[N];
			for(int j=0;j<N;j++)
				list[j]=kbd.next();
			res[i]=solve(list);
		}
		for(int i=0;i<res.length;i++)
			System.out.println(res[i]);
	}
	static String solve(String[]list) {
		String str=list[0];
		for(int i=1;i<list.length;i++) {
			if(list[i].charAt(0)<=str.charAt(0))
				str=list[i].charAt(0)+str;
			else
				str=str+list[i].charAt(0);
		}
		return str;
	}

}
