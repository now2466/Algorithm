from collections import deque
progresses = [95, 90, 99, 99, 80, 99]
speeds = [1,1,1,1,1,1]
def solution(progresses,speeds):
    answer = []
    n = len(progresses)
    queue = deque()
    for i in range(n):
        queue.append([progresses[i],i])
    while queue:
        count = 0
        for i in range(n):
            if progresses[i] <100:
                progresses[i]+=speeds[i]
        while queue and progresses[queue[0][1]]>=100:
            queue.popleft()
            count+=1
        if count>0:
            answer.append(count)
    return answer

print(solution(progresses,speeds))

