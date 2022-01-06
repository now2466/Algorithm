import math
import sys
input = sys.stdin.readline
n, m = map(int,input().split())

loc = [0]
for _ in range(n):
    loc.append(list(map(int,input().split())))
unf = [i for i in range(n+1)]

def find(a):
    if unf[a]==a:
        return a
    else:
        fa = find(unf[a])
        unf[a]=fa
        return unf[a]
def union(a,b):
    fa = find(a)
    fb = find(b)

    if fa!=fb:
        unf[fa]=fb


for _ in range(m):
    a, b = map(int,input().split())
    union(a,b)
dist = []
for i in range(1,n+1):
    for j in range(i,n+1):
        if i!=j:
            d = math.sqrt((loc[i][0]-loc[j][0])**2+(loc[i][1]-loc[j][1])**2)

            dist.append([i,j,d])

dist.sort(key = lambda x: x[2])

cost = 0
cnt = n-1
for a,b,c in dist:
    if find(a)!=find(b):
        union(a,b)
        cost+=c
        cnt-=1
    if cnt==0:
        break
print("%.2f"%cost)
