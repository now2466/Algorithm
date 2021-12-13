n = int(input())
m = int(input())

graph=[]

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
        unf[fb]=fa
    
for _ in range(m):
    a,b,c = list(map(int,input().split()))
    graph.append([a,b,c])

graph.sort(key = lambda x:x[2])
answer = 0
count = 0
print(graph)
for a,b,c in graph:
    if find(a)!=find(b):
        answer+=c
        union(a,b)
        print(unf)
        count+=1
        if count==n-1:
            break
    

print(answer)
