n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

answer = 0
check = [0]*(n+1)
def DFS(v):
    global answer
    answer+=1
    for nv in graph[v]:
        if check[nv]==0:
            check[nv]=1
            DFS(nv)
check[1]=1
DFS(1)
print(answer-1)
