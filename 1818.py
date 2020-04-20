#1818
N=int(input())
book=list(map(int,input().split()))
#space로 여러개의 숫자 입력받아 정수 리스트에 저장
arr=[]
# LIS알고리즘
# 가장 긴 증가하는 부분수열의 길이를 찾아
# 전체에서 그 길이를 제외한 만큼을 구하면
# 그게 바로 최소횟수로 정리하는 법.
for num in book:
    if (len(arr)==0 or arr[len(arr)-1]<num):
        arr.append(num)
    else:
        i=0
        j=len(arr)-1
        while i<j:
            mid=(int)((i+j)/2)
            if arr[mid]<num:
                i=mid+1
            else:
                j=mid
        arr[j]=num
# arr은 최장 부분수열의 길이
print(N-len(arr))
