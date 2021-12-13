costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
n = 4

unf = [i for i in range(n+1)]

def find(v):
    if v==unf[v]:
        return v
    else:
        unf[v] = find(unf[v])
        return unf[v]
def union(a,b):
    fa = find(a)
    fb = find(b)

    if fa != fb:
        unf[fa] = fb

costs.sort(key = lambda x:x[2])
answer = 0
count = 0
for a, b, c in costs:
    if find(a)==find(b):
        continue
    else:
        answer+=c
        union(a,b)
        count+=1
    if count==n-1:
        break
print(answer)
print(unf)
