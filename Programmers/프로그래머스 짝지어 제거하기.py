def solution(s):
    from collections import deque

    queue = deque(s)

    temp = []

    while queue:
        if temp:
            if temp[-1]==queue[0]:
                temp.pop()
                queue.popleft()
        else:
            temp.append(queue.popleft())

    if temp:
        return 0
    else:
        return 1
