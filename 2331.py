#2331
#dfs bfs
"""
def sum(x):
    res=0
    for i in str(x):
        res+=int(i)**P
    return res
A,P=input().split()
A=int(A)
P=int(P)
lst=[]
lst.append(A)
i=0
s=0
while s not in lst[0:i]:
    s=sum(lst[i])
    lst.append(s)
    i+=1
del lst[-1]
count=0
for j in lst:
    if j is s: break
    else: count+=1
print(count)
"""
# 0 -> 거짓
# 0 제외 정수 -> 참
MAX=300001
def dfs(num):
    visited[num]+=1
    if visited[num]==3:# 3이어야 사이클이 생긴 것을 확인할 수 있음
        return
    sum=0
    while num:
        sum+=(int)(num%10)**P
        num=num/10
    dfs(sum)

A,P=input().split()
A=int(A)
P=int(P)
visited=[0 for _ in range(MAX)]
dfs(A)
result=0
for i in range(MAX):
    if visited[i]==1:
        result+=1
print(result)