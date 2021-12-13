import sys
n, m = map(int,input().split())
edges = []
for _ in range(m):
    edges.append(list(map(int,sys.stdin.readline().split())))
unf = [i for i in range(n+1)]

def find(v):
    if v==unf[v]:
        return v
    else:
        unf[v]=find(unf[v])
        return unf[v]
def union(a,b):
    fa = find(a)
    fb = find(b)

    if fa>fb:
        unf[fa]=fb
    else:
        unf[fb]=fa

edges.sort(key = lambda x:[x[2],x[0],x[1]])
answer=0
count=0
maxn=0

for a,b,c in edges:
    if find(a)!=find(b):
        answer+=c
        union(a,b)
        count+=1
        if count==n-2:
            break
print(answer)
