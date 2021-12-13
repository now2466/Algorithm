import sys
import collections
import heapq
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

dy = [float('inf')]*(n+1)
graph=collections.defaultdict(list)
for _ in range(m):
    a,b,c = map(int,sys.stdin.readline().split())
    graph[a].append([b,c])

s, e = map(int,sys.stdin.readline().split())

queue = []
heapq.heappush(queue,[s,0])

while queue:
    point , cost = heapq.heappop(queue)

    if dy[point]<cost:
        continue
    for np, nc in graph[point]:
        if dy[np]>cost+nc:
            dy[np]=cost+nc
            heapq.heappush(queue,[np,cost+nc])

print(dy[e])

    

