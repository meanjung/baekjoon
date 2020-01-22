package 자료구조;
import java.util.*;
public class java12865 {
 
    public static void main(String[] args) {
        Scanner kbd=new Scanner(System.in);
        int N=kbd.nextInt();
        int K=kbd.nextInt();
        int value[]=new int[N+1];
        int weight[]=new int[N+1];
        for(int i=1;i<=N;i++) {
            weight[i]=kbd.nextInt();
            value[i]=kbd.nextInt();
        }
        int dp[][]=new int[N+1][K+1];
        for(int i=0;i<N+1;i++)
            for(int j=0;j<K+1;j++)
                dp[i][j]=0;
        
        for(int i=1;i<=N;i++) {
            for(int j=1;j<=K;j++) {
                dp[i][j]=dp[i-1][j];
                if(j-weight[i]>=0)
                    dp[i][j]=max(dp[i][j],dp[i-1][j-weight[i]]+value[i]);
            }
        }
        System.out.println(dp[N][K]);
    }
    static int max(int a, int b) {
        if(a<b) return b;
        else return a;
    }
 
}