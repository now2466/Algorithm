from collections import deque
n , m = map(int,input().split())
nums = list(map(int,input().split()))

answer = 0

queue = deque()
for i in range(n):
    queue.append([i+1,nums[i]])

while queue:
    idx, sumn = queue.popleft()
    if sumn == m:
        answer+=1
    
    for i in range(idx,n):
        queue.append([i+1,sumn+nums[i]])

print(answer)
                
