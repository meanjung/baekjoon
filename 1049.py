# 1049
# 그리디
import sys

N,M=map(int,sys.stdin.readline().split())
brand=[]
for i in range(M):
    brand.append(list(map(int,sys.stdin.readline().split())))
q=N//6 #몫
r=N%6 #나머지
set_min=min(brand[i][0] for i in range(M))
single_min=min(brand[i][1] for i in range(M))
res=0
if q==0:
    res+=min(set_min, single_min*N)
else:
    if set_min*q>single_min*q*6:
        res+=single_min*q*6
    else:
        res+=set_min*q
    if set_min>single_min*r:
        res+=single_min*r
    else:
        res+=set_min
print(res)