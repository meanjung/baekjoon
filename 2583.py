#2583
from collections import deque
def bfs(start, end):
    q=deque()
    q.append([start,end])
    while q:
        x=q.popleft()
        visited[x[0]][x[1]]=True
        for i in range(4):
            lx=x[0]+dx[i]
            ly=x[1]+dy[i]
            if 0<=lx<M and 0<=ly<N:
                if monun[lx][ly]==0:
                    if visited[lx][ly]==False:
                        q.append([lx,ly])
                        visited[lx][ly]=True
        groups[group_id]+=1

M,N,K=map(int,input().split())
monun=[[0 for cols in range(N)] for rows in range(M)]
for i in range(K):
    x1,y1,x2,y2=map(int,input().split())
    for j in range(x1,x2):
        for k in range(y1,y2):
            monun[k][j]=1

dx=[0,1,0,-1]
dy=[1,0,-1,0]
groups=[0]*(M*N)
group_id=0
visited=[[0 for cols in range(N)] for rows in range(M)]
for i in range(M):
    for j in range(N):
        if monun[i][j]==0 and visited[i][j]==False:
            bfs(i,j)
            group_id+=1
groups.sort()
print(group_id)
for i in groups:
    if i!=0:
        print(i, end=' ')