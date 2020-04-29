#11049
#dp
#시간초과 오류 - 일단 오류가 뜨기때문에 로직이 맞는지 확신할 수 없음
#논리만이라도 중요하게 보기
import sys
from test.test_os import INT_MAX
N=int(sys.stdin.readline())
lst=[]
for i in range(N):
    r,c=map(int, sys.stdin.readline().split())
    lst.append([r,c])
dp=[[0 for cols in range(N)] for rows in range(N)]
for i in range(N):
    for j in range(i+1,N): # 항상 j>=i
        minimum=INT_MAX
        for k in range(i,j):
            cv=dp[i][k]+dp[k+1][j]+lst[i][0]*lst[k][1]*lst[j][1]
            if cv<minimum:
                minimum=cv
        dp[i][j]=minimum
print(dp[0][N-1])
