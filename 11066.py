#11066
#dp
import sys
T=int(sys.stdin.readline())
for i in range(T):
    K=int(sys.stdin.readline())
    lst=list(map(int,sys.stdin.readline().split()))
    # dp 초기화
    dp=[[0 for _ in range(K)] for _ in range(K)]
    for i in range(K-1):
        dp[i][i+1]=lst[i]+lst[i+1]
        for j in range(i+2,K):
            dp[i][j]=dp[i][j-1]+lst[j]
            # 여기까지 일단 초기화
    for d in range(2,K):
        for i in range(K-d):
            j=i+d
            minimum=[dp[i][k] + dp[k+1][j] for k in range(i,j)]
            dp[i][j]+=min(minimum)
    print(dp[0][K-1])