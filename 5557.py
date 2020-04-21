#5557
#dp

import sys

N=int(sys.stdin.readline())
lst=list(map(int,sys.stdin.readline().split()))

dp=[[0 for cols in range(21)] for rows in range(N-1)]

for i in range(N-1):
    if i==0:
        dp[i][lst[i]]=1
        continue
    for j in range(21):
        prev=dp[i-1][j]
        if prev!=0:
            if j-lst[i]>=0:
                dp[i][j-lst[i]]+=prev
            if j+lst[i]<=20:
                dp[i][j+lst[i]]+=prev
print(dp[N-2][lst[N-1]])
