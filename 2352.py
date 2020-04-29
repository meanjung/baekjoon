#2352
#dp인데 lis
import sys
n=int(sys.stdin.readline())
lst=[]
lst.extend(list(map(int,sys.stdin.readline().split())))
res=[]
for num in lst:
    # res가 비어있거나 res의 마지막 값보다 num이 크다면
    # 그냥 append
    if len(res)==0 or res[len(res)-1]<num:
        res.append(num)
    else:
        i=0
        j=len(res)-1
        while i<j:
            mid=(int)((i+j)/2)
            if res[mid]<num:
                i=mid+1
            else:
                j=mid
        res[j]=num
print(len(res))

