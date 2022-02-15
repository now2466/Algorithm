from collections import deque
n, m = map(int,input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)


check=[0]*(n+1)

        
def bfs(node):
    q = deque()
    q.append(node)
    check[node]=1
    while q:
        node = q.popleft()
        for n in graph[node]:
            if check[n]==0:
                check[n]=check[node]+1
                q.append(n)

bfs(1)
m = max(check)

dist = max(check)
count = check.count(dist)
idx = check.index(dist)
print(idx,dist-1,count)
