# 9251
# LCS
# 시간초과
import sys
str1=[x for x in sys.stdin.readline().strip('\n')]
str2=[x for x in sys.stdin.readline().strip('\n')]
#str1=sys.stdin.readline().strip('\n')
#str2=sys.stdin.readline().strip('\n')
len1=len(str1)
len2=len(str2)
dp=[[0]*(len1+1) for _ in range(len2+1)]

for i in range(1,len1+1):
    for j in range(1,len2+1):
        if str1[i-1]==str2[j-1]:
            dp[i][j]=dp[i-1][j-1]+1;
        else:
            dp[i][j]=max(dp[i][j-1],dp[i-1][j])
print(dp[-1][-1])