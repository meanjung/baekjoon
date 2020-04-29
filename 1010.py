#1010
#dp
import sys

dp=[[0 for cols in range(30)] for rows in range(30)]
for i in range(30):
    dp[1][i]=i
for i in range(2,30):
    for j in range(i,30):
        for k in range(i-1,j):
            dp[i][j]+=dp[i-1][k]

T=int(sys.stdin.readline())
for i in range(T):
    N,M=map(int,sys.stdin.readline().split())
    print(dp[N][M])