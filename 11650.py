#11650
N=int(input())
xy_list=[]
for i in range(N):
    a,b=input().split()
    xy_list.append([int(a),int(b)])
xy_list.sort()
for i in range(len(xy_list)):
    print(xy_list[i][0],xy_list[i][1])