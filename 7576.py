#7576
from collections import deque
#import numpy as np
M,N=map(int,input().split())
tomato=[[int(y) for y in input().split()] for x in range(N)]
dx=[0,1,0,-1]
dy=[1,0,-1,0]
visited=[[0 for cols in range(M)] for rows in range(N)]
time=[[0 for cols in range(M)] for rows in range(N)]

q=deque()

for i in range(N):
    for j in range(M):
        if tomato[i][j]==1:
            q.append([i,j])

while q:
    a=q.popleft()
    x=a[1]
    y=a[0]
    visited[y][x]=True
    for i in range(4):
        lx=x+dx[i]
        ly=y+dy[i]
        if 0<=lx and lx<M and 0<=ly and ly<N:
            if tomato[ly][lx]==0 and visited[ly][lx]==False:
                tomato[ly][lx]=1
                time[ly][lx]=time[y][x]+1
                q.append([ly,lx])
if any(0 in x for x in tomato):
    print('-1')
else:
    #print(np.amax(time))
    print(max(map(max,time)))
