#1697
from collections import deque
LIMIT=100001
def solve(arr,n,k):
    q=deque()
    q.append(n)
    while q:
        i=q.popleft()
        if i==k:
            return arr[i]
        for j in (i+1, i-1, 2*i): #컨테이너에 있는 값들이 순서대로 변수에 대입된다.
            if 0<=j<LIMIT and arr[j]==0:
                arr[j]=arr[i]+1
                q.append(j)

# 코딩테스트에서 시간 단축을 위함
N,K=input().split()
N=int(N)
K=int(K)
find=[0]*LIMIT
print(solve(find,N,K))


