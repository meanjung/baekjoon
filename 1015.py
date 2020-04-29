# 1015
# 정렬
import sys
N=int(sys.stdin.readline())
A=list(map(int,sys.stdin.readline().split()))
sorted_A=[i for i in A]
sorted_A.sort()
P=[]
for i in A:
    P.append(sorted_A.index(i))
    sorted_A[sorted_A.index(i)]=-1

for i in P:
    print(i, end=" ")