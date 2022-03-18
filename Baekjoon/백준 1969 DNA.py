n, m = map(int,input().split())
import collections
dna = []
for _ in range(n):
    dna.append(input())


answer = ""
count = 0
for i in range(m):
    A = 0
    C = 0
    G = 0
    T = 0
    for j in range(n):
        if dna[j][i] == 'A':
            A+=1
        elif dna[j][i] == 'C':
            C+=1
        elif dna[j][i] == 'G':
            G+=1
        elif dna[j][i] == 'T':
            T+=1
    mc = max(A,C,G,T)
    if A==mc:
        answer+="A"
    elif C==mc:
        answer+="C"
    elif G==mc:
        answer+="G"
    elif T==mc:
        answer+="T"
    count+=n-mc

print(answer)
print(count)

