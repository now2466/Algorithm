n = int(input())
s = list(map(int,input().split()))

sumn = sum(s)
ch = [0]*(sumn+2)

def DFS(idx,total):
    ch[total]=1
    for i in range(idx,n):
        DFS(i+1,total+s[i])

for i in range(n):
    DFS(i+1,s[i])

for i in range(1,sumn+2):
    if ch[i]==0:
        print(i)
        break
print(ch)
