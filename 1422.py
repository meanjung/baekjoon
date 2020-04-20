#1422
K, N=input().split()
K=int(K)
N=int(N)
numlist=[]
for i in range(K):
    t=int(input())
    numlist.append(t)
numlist.sort(reverse=True)
string=''
if K==N:
    for i in numlist:
        string+=str(i)
else:
    for i in numlist:
        string+=str(i)
    for i in range(N-K):
        string=str(numlist[0])+string
print(string)
