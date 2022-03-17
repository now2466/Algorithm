from collections import deque
import sys
queue = deque()

n, k = map(int,sys.stdin.readline().split())

queue.append(n)

ch = [0]*100001
ch[n] = 1
dist = [float('inf')]*100001
dist[n]=0
while queue:
    now = queue.popleft()

    for nx in [now-1,now+1,2*now]:
        if -1<= nx<100001 and ch[nx]==0:
            if nx == 2*now:
                ch[nx]=1
                dist[nx]=dist[now]
                queue.appendleft(nx)
                
            else:
                ch[nx]=1
                dist[nx]=dist[now]+1
                queue.append(nx)
          
print(dist[k])   
