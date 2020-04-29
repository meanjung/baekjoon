# 1065
# 브루트 포스
# 탐색
import sys

def check(x):
    str_x=str(x)
    lst=[(int(str_x[i+1])-int(str_x[i])) for i in range(len(str_x)-1)]
    for i in range(1,len(lst)):
        if lst[i]!=lst[0]:
            return False
    return True

N=int(sys.stdin.readline())
res=0
if N<=99:
    res+=N
else:
    res+=99
    for i in range(100,N+1):
        if check(i)==True:
            res+=1
        else:
            continue
print(res)


