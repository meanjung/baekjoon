#2606
from collections import deque
N=int(input()) #컴퓨터의 수
P=int(input()) #컴퓨터 쌍의 수
#바이러스에 감염된 컴퓨터의 수 출력하라
lst=[[0 for cols in range(N+1)] for rows in range(N+1)]
for i in range(P):
    x,y=map(int,input().split())
    lst[x][y]=1
    lst[y][x]=1
visited=[0]*(N+1)
q=deque()
for i in range(N+1):
    if lst[1][i]==1:
        q.append(i)
while q:
    x=q.popleft()
    visited[x]=True
    for i in range(N+1):
        if lst[x][i]==1 and visited[i]==False:
            q.append(i)
count=0
for i in range(len(visited)):
    if visited[i]==True:
        count+=1
print(count-1)