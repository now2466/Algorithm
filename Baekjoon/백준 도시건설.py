n, m = map(int,input().split())
import sys
graph = []
sumn=0
for _ in range(m):
    a,b,c = list(map(int,sys.stdin.readline().split()))
    graph.append([a,b,c])
    sumn+=c

answer = 0
unf = [i for i in range(n+1)]
def find(a):
    if a==unf[a]:
        return a
    else:
        unf[a]=find(unf[a])
        return unf[a]
def union(a,b):
    fa = find(a)
    fb = find(b)

    if fa!=fb:
        unf[fa]=fb
graph.sort(key = lambda x:x[2])
count = 0

for a,b,c in graph:
    if find(a)!=find(b):
        answer+=c
        union(a,b)
        count+=1
        if count==n-1:
            break
else:
    print(-1)
    sys.exit(0)
    
print(sumn-answer)
