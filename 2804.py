#2804
A,B=input().split()
for i in A:
    if i in B:
        start_a=A.find(i)
        start_b=B.find(i)
        break
for i in range(len(B)):
    string=''
    if i is start_b:
        string=A
    else:
        for j in range(0,start_a):
            string+='.'
        string+=B[i]
        for j in range(start_a+1,len(A)):
            string+='.'
    print(string)
