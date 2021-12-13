n = int(input())

nums = [i for i in range(10)]

sign = list(map(str,input().split()))

res = [11]*10

maxn = "0"
minn = "999999999999999"
def DFS(level):
    global maxn, minn
    if level>len(sign):
        temp = "".join(map(str,res[:level]))
        if int(temp)>int(maxn):
            maxn=temp
        if int(temp)<int(minn):
            minn=temp
    else:
        for x in nums:
            if ch[x]==0:
                if sign[level-1]=="<" and res[level-1]<x:
                    ch[x]=1
                    res[level] = x
                    DFS(level+1)
                    ch[x]=0
                elif sign[level-1]==">" and res[level-1]>x:
                    ch[x]=1
                    res[level]=x
                    DFS(level+1)
                    ch[x]=0

for i in range(10):
    ch=[0]*10
    ch[i]=1
    res[0]=i
    DFS(1)
print(maxn)
print(minn)
    
