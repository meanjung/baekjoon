#2667
def dfs_stack(start, end):
    s=[]
    s.append([start,end])
    visited[start][end]=True
    groups[group_id]+=1
    while True:
        if not s: # 스택이 비어있다면
            break
        x=s[-1][0]
        y=s[-1][1]
        s.pop()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx and nx<N and 0<=ny and ny<N:
                if house[nx][ny]==1 and visited[nx][ny]==False:
                    visited[nx][ny]=True
                    groups[group_id]+=1
                    s.append([nx,ny])

N=int(input())
house=[]
for i in range(N):
    lst=list(map(int, str(input()))) #띄어쓰기없이 정수 입력받아 2차원배열로 저장
    house.append(lst)
visited=[[0 for col in range(N)] for row in range(N)]
dx=[-1,0,1,0]
dy=[0,1,0,-1]
groups=[0]*625
group_id=0

for i in range(N):
    for j in range(N):
        if house[i][j]==1 and visited[i][j]==False:
            group_id+=1
            dfs_stack(i,j)
groups.sort()
count=0
for i in groups:
    if i != 0:
        count+=1
print(count)
for i in groups:
    if i != 0:
        print(i)