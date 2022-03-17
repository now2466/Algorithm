import heapq
import sys
n, m = map(int,sys.stdin.readline().split())
points = list(map(int,sys.stdin.readline().split()))

graph = [[] for _ in range(n)]

dist = [float('inf')]*n
heap = []
for _ in range(m):
    a, b, c = map(int,sys.stdin.readline().split())

    graph[a].append([b,c])
    graph[b].append([a,c])

dist[0]=0
heapq.heappush(heap,[0,0])

while heap:
    cost, now = heapq.heappop(heap)

    if dist[now] < cost:
        continue

    for np, nc in graph[now]:
        if nc + cost < dist[np] and (points[np]==0 or np==n-1):
            dist[np] = cost+ nc
            heapq.heappush(heap,[dist[np],np])
if dist[n-1]!=float('inf'):
    print(dist[n-1])
else:
    print(-1)
