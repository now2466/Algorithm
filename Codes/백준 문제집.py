import heapq
n, m = map(int,input().split())
indegree = [0]*(n+1)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    indegree[b]+=1
    graph[a].append(b)


heap=[]
print(graph)
print(indegree)
for i in range(1,n+1):
    if indegree[i]==0:
        heapq.heappush(heap,i)
answer = []
while heap:
    x = heapq.heappop(heap)
    answer.append(x)
    for nx in graph[x]:
        indegree[nx]-=1
        if indegree[nx]==0:
            heapq.heappush(heap,nx)
                
for x in answer:
    print(x,end=" ")
