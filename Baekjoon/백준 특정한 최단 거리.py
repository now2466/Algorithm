import heapq
import sys
n,m = map(int,sys.stdin.readline().split())


heap = []
graph= [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int,sys.stdin.readline().split())

    graph[a].append([b,c])
    graph[b].append([a,c])

v1, v2 = map(int,sys.stdin.readline().split())


def dijkstra(start,end):
    dist = [float('inf')]*(n+1)
    dist[start]=0
    heapq.heappush(heap,[0,start])#cost, 현재정점, v1과 v2를 거쳤는지 여부

    while heap:
        cost, x= heapq.heappop(heap)
        
        if cost > dist[x]:
            continue
        for nx,nc in graph[x]:
            if nc + cost < dist[nx]:
                dist[nx] = cost + nc
                heapq.heappush(heap,[dist[nx],nx])
    return dist[end]

path1 = dijkstra(1,v1) + dijkstra(v1,v2) + dijkstra(v2,n)
path2 = dijkstra(1,v2) + dijkstra(v2,v1) + dijkstra(v1,n)
if path1 == float('inf') and path2 ==float('inf'):
    print(-1)
else:
    print(min(path1,path2))
