# 14500
# 브루트포스

import sys

def find(x,y):
    global answer
    for i in range(19):
        result=0
        for j in range(4):
            try:
                dx=x+tetromino[i][j][0]
                dy=y+tetromino[i][j][1]
                result+=lst[dx][dy]
            except IndexError:
                continue
        answer=max(answer,result)

tetromino = [
    [(0,0), (0,1), (1,0), (1,1)], # ㅁ
    [(0,0), (0,1), (0,2), (0,3)], # ㅡ
    [(0,0), (1,0), (2,0), (3,0)], # ㅣ
    [(0,0), (0,1), (0,2), (1,0)], 
    [(1,0), (1,1), (1,2), (0,2)],
    [(0,0), (1,0), (1,1), (1,2)], # ㄴ
    [(0,0), (0,1), (0,2), (1,2)], # ㄱ
    [(0,0), (1,0), (2,0), (2,1)],
    [(2,0), (2,1), (1,1), (0,1)],
    [(0,0), (0,1), (1,0), (2,0)], 
    [(0,0), (0,1), (1,1), (2,1)],
    [(0,0), (0,1), (0,2), (1,1)], # ㅜ
    [(1,0), (1,1), (1,2), (0,1)], # ㅗ
    [(0,0), (1,0), (2,0), (1,1)], # ㅏ
    [(1,0), (0,1), (1,1), (2,1)], # ㅓ
    [(1,0), (2,0), (0,1), (1,1)],
    [(0,0), (1,0), (1,1), (2,1)],
    [(1,0), (0,1), (1,1), (0,2)],
    [(0,0), (0,1), (1,1), (1,2)]
]

N,M=map(int,sys.stdin.readline().split())
lst=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]

answer=0

for i in range(N):
    for j in range(M):
        find(i,j)
print(answer)