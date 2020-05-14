# 10814
# counting sort
def sort(arr):
    ages=[0]*201
    for i in range(len(arr)):
        ages[arr[i][0]]+=1
    for i in range(0,max(arr[i][0] for i in range(len(arr)))):
        ages[i+1]+=ages[i]
    B=[0]*len(arr)
    for i in range(len(arr)-1,-1,-1):
        ages[arr[i][0]]-=1
        B[ages[arr[i][0]]]=[arr[i][0], arr[i][1]]
    for k in range(len(B)):
        print(B[k][0], B[k][1])

import sys
members=[]
for _ in range(int(sys.stdin.readline())):
    age, name=map(str,sys.stdin.readline().split())
    age=int(age)
    members.append([age, name])
sort(members)
