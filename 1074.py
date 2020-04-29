# 1074
# 분할정복
import sys
N,r,c=map(int,sys.stdin.readline().split())
num=0
while N>0:
    temp=(2**N)//2
    if N>1:
        if temp>r and temp<=c:
            num+=(temp**2)
            c-=temp
        elif temp<=r and temp>c:
            num+=(temp**2)*2
            r-=temp
        elif temp<=r and temp<=c:
            num+=(temp**2)*3
            c-=temp
            r-=temp
    elif N==1:
        if r==0 and c==1:
            num+=1
        elif r==1 and c==0:
            num+=2
        elif r==1 and c==1:
            num+=3
    N-=1
print(num)