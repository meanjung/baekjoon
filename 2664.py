#2664
#검색의 도움을 조금 받긴 했지만 충분히 고민했다.
from collections import deque
n=int(input())
x,y=map(int, input().split())
m=int(input())
lst=[[0 for cols in range(n+1)] for rows in range(n+1)]
visited=[0]*(n+1)
depth=[0]*(n+1)
for _ in range(m):
    f,s=map(int, input().split())
    lst[f][s]=1
    lst[s][f]=1

s=deque()
s.append(x)
flag=0
while s:
    p=s.popleft()
    visited[p]=True
    for i in range(1,n+1):
        if lst[p][i]==1 and visited[i]==False:
            depth[i]=depth[p]+1
            s.append(i)
            if i==y: 
                flag=1
                break
    if flag==1:
        break

if flag==0:
    print('-1')
else:
    print(depth[y])


