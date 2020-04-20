# 2468
# 잠기지 않는 영역의 개수를 구해야 함
def dfs(start,end,k):
    s=[] #스택
    s.append([start,end])
    visited[start][end]=True #일단 방문한 것 표시
    while True:
        if not s:
            break
        x=s[-1][0]
        y=s[-1][1]
        s.pop()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx and nx<N and 0<=ny and ny<N:
                if apt[nx][ny]>k and visited[nx][ny]==False:
                    visited[nx][ny]=True
                    s.append([nx,ny])

N=int(input())
dx=[-1,0,1,0]
dy=[0,-1,0,1]
apt=[[int(x) for x in input().split()] for y in range(N)] #띄어쓰기 있게 이차원배열 입력
max_value=max(map(max, apt))
min_value=min(map(min,apt))
groups=[0]*max_value
for k in range(max_value+1):
    visited=[[0 for cols in range(N)] for rows in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j]==False and apt[i][j]>k:
                dfs(i,j,k)
                groups[k]+=1

print(max(groups))
