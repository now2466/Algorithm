from collections import deque
def solution(priorities,location):
    queue = deque()

    for i in range(len(priorities)):
        if i == location:
            queue.append([priorities[i],1])
        else:
            queue.append([priorities[i],0])
    count = 0
    while queue:
        x, flag = queue.popleft()
        if queue and x<max(queue)[0]:
            queue.append([x,flag])
        else:
            count+=1
            if flag==1:
                return count

print(solution([2],0))
                
