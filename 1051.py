# 1051
# 브루트 포스
import sys
N,M=map(int, sys.stdin.readline().split())
sq=[]
for i in range(N):
    sq.append(list(map(int,sys.stdin.readline().strip())))
max_v=0
for i in range(N):
    for j in range(M):
        for k in range(min(N,M)):
            if i+k<N and j+k<M:
                if sq[i][j]==sq[i+k][j] and sq[i][j]==sq[i][j+k] and sq[i][j]==sq[i+k][j+k]:
                    if max_v<k:
                        max_v=k
print((max_v+1)**2)
