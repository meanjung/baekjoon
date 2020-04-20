#9466
def dfs(x):
    global result
    visited[x]=True
    cycle.append(x)
    number=numbers[x]
    if visited[number]: # 사이클이 마무리되었다면
        if number in cycle: # 사이클이 형성되었는지 판단하는 것
            result+=cycle[cycle.index(number):]
        return
    else:
        dfs(number)

   
test_case=int(input())
for i in range(test_case):
    stu_num=int(input()) # 학생수
    numbers=[0]+list(map(int,input().split()))
    visited=[True]+[False]*stu_num
    result=[]
    for j in range(1,stu_num+1):
        if not visited[j]: # 방문 안한 곳이라면
            cycle=[]
            dfs(j)
    print(stu_num-len(result))





