n , m = map(int, input().split())

like = [[]for _ in range(n)]

for i in range(n):
    x = list(map(int,input().split()))
    like[i]=x

com_list = []
res=[0]*3
def DFS(level,start):
    if level ==3:
        temp=[]
        for x in res:
            temp.append(x)
        com_list.append(temp)
        
    else:
        for i in range(start,m):
            res[level]=i
            DFS(level+1,i+1)

DFS(0,0)
answer=0
for i in range(len(com_list)):
    sumN=0
    for j in range(n):
        maxN=0
        for k in range(3):
            idx = com_list[i][k]
            maxN=max(maxN,like[j][idx])
        sumN+=maxN
    answer=max(answer,sumN)

print(answer)




