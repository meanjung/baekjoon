#2941
string=input()
check=['c=','c-','d-','lj','nj','s=','z=']
i=0
count=0;
while i<=(len(string)-1):
    if string[i:i+2] in check:
        count+=1
        i+=2
    elif string[i:i+3]=='dz=':
        count+=1
        i+=3
    else:
        count+=1
        i+=1
print(count)