package 자료구조;
import java.util.*;
public class java11375 {
	static int visit[];
	static int person[][];
	static int work[];
	
	public static void main(String[] args) {
		Scanner kbd=new Scanner(System.in);
		int N=kbd.nextInt();//직원수
		int M=kbd.nextInt();//일의 개수
		person=new int[N+1][M+1];
		visit=new int[N+1];
		work= new int[N+1];
		int res=0;
		for(int i=1;i<N+1;i++) {//배열 입력받기
			person[i][0]=kbd.nextInt();
			for(int j=1;j<=person[i][0];j++)
				person[i][j]=kbd.nextInt();
			for(int j=1;j<=N;j++) visit[j]=0;
			res+=bmatch(i);
		}
		System.out.println(res);
			
	}
	static int bmatch(int p) {
		int w;
		if(visit[p]!=0) return 0;
		visit[p]=1;
		
		for(int i=1;i<=person[p][0];i++) {
			w=person[p][i];
			if(work[w]==0||bmatch(work[w])!=0) {
				work[w]=p;
				return 1;
			}
		}
		return 0;
	}
	

}
