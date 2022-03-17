import heapq

n, m, k, x = map(int,input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int,input().split())

    graph[a].append(b)

dist = [float('inf')]*(n+1)
heap = []
dist[x]=0
heapq.heappush(heap,x)
while heap:
    now = heapq.heappop(heap)

    
    for nx in graph[now]:
        if dist[now] + 1 < dist[nx]:
            dist[nx] = dist[now] + 1
            heapq.heappush(heap,nx)
answer = []

for i in range(len(dist)):
    if dist[i]==k:
        answer.append(i)

if len(answer)==0:
    print(-1)
else:
    for x in answer: print(x)
