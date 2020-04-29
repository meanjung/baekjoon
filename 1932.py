#1932
#dp
#두 번째 풀어본 것
import sys
n=int(sys.stdin.readline())
lst=[]
for i in range(n):
    lst.append(list(map(int,sys.stdin.readline().split())))
for i in range(1,n):
    for j in range(i+1):
        if j==0:
            lst[i][j]+=lst[i-1][j]
        elif i==j:
            lst[i][j]+=lst[i-1][j-1]
        else:
            lst[i][j]+=max(lst[i-1][j-1],lst[i-1][j])
print(max(lst[n-1]))