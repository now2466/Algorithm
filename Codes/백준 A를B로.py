from collections import deque
a = str(input())
b = str(input())
n = len(a)
queue = deque()

queue.append([a,0])

if len(a)==1:
    if a==b:
        print(0)
    else:
        print(-1)
else:
    while queue:
        x, count = queue.popleft()
        if x==b:
            print(count)
            break
        if count>n:
            print(-1)
            break
        for i in range(1,n):
            temp = x[i]+x[:i]+x[i+1:]
            if temp not in queue:
                queue.append([temp,count+1])

        
