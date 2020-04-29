# 1021
# 정렬 탐색
import sys
from collections import deque

N,M=map(int,sys.stdin.readline().split())
lst=deque()
for x in range(1,N+1):
    lst.append(x)
nums=list(map(int,sys.stdin.readline().split()))
count=0
for i in nums:
    if lst.index(i)>len(lst)-1-lst.index(i):
        while lst[0]!=i:
            lst.appendleft(lst.pop())
            count+=1
    else:
        while lst[0]!=i:
            lst.append(lst.popleft())
            count+=1
    lst.popleft()
print(count)
