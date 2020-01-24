package 자료구조;
import java.util.*;
public class java2293 {

	public static void main(String[] args) {
		Scanner kbd=new Scanner(System.in);
		int n=kbd.nextInt();
		int k=kbd.nextInt();
		int coin[]=new int[n+1];
		int dp[][]=new int[n+1][k+1];
		for(int i=1;i<n+1;i++)
			coin[i]=kbd.nextInt();
		//dp초기화
		for(int i=0;i<n+1;i++)
			for(int j=0;j<k+1;j++)
				dp[i][j]=0;
		for(int i=0;i<n+1;i++)
			dp[i][0]=1;
		//결과 도출
		for(int i=1;i<n+1;i++) {
			for(int j=1;j<k+1;j++) {
				if(j>=coin[i])
					dp[i][j]=dp[i-1][j]+dp[i][j-coin[i]];
				else dp[i][j]=dp[i-1][j];
			}
		}
		System.out.println(dp[n][k]);
		
	}
	

}
