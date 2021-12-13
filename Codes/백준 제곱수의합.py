import math
n = int(input())

dy = [i for i in range(n+1)]

for i in range(1,n+1):
    j=0
    dy[i]=i
    while j*j<=i:
        if dy[i] > dy[i-j*j]+1:
            dy[i] = dy[i-j*j]+1
        j+=1

print(dy[n])
