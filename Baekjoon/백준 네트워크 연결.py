n = int(input())
m = int(input())
edges = []
for _ in range(m):
    x = list(map(int,input().split()))
    edges.append(x)

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
    if fa!=fb:
        unf[fa]=fb

edges.sort(key = lambda x:x[2])
answer = 0
count = 0
for a,b,c in edges:
    if find(a)!=find(b):
        answer+=c
        count+=1
        union(a,b)
    if count>=n-1:
        break
print(answer)
