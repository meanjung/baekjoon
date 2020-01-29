package 자료구조;
import java.util.*;
public class java13416 {

	public static void main(String[] args) {
		Scanner kbd=new Scanner(System.in);
		int T=kbd.nextInt();
		int res[]=new int[T];
		int N;
		for(int i=0;i<T;i++) {
			N=kbd.nextInt();
			int A[]=new int[N];
			int B[]=new int[N];
			int C[]=new int[N];
			for(int j=0;j<N;j++) {
				A[j]=kbd.nextInt();
				B[j]=kbd.nextInt();
				C[j]=kbd.nextInt();
			}
			res[i]=solve(A,B,C);
		}
		for(int i=0;i<res.length;i++)
			System.out.println(res[i]);
	}
	static int solve(int[]A, int[]B,int[]C) {
		int sum=0;
		for(int i=0;i<A.length;i++) {
			if(A[i]<0&&B[i]<0&&C[i]<0) continue;
			sum+=Math.max(A[i], Math.max(B[i], C[i]));
		}
		return sum;
	}

}
