from collections import deque

def solution(maps):
    queue = deque()

    n = len(maps)
    m = len(maps[0])

    dx = [-1,0,1,0]
    dy = [0,-1,0,1]

    queue.append([0,0])

    cost = [[-1]*m for _ in range(n)]
    cost[0][0]=1

    while queue:
        x,y = queue.popleft()

        if x==n-1 and y == m-1:
            return cost[x][y]


        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if 0<=nx<n and 0<=ny<m: 
                if cost[nx][ny]==-1: 
                    if maps[nx][ny]==1:
                        cost[nx][ny]=cost[x][y]+1
                        queue.append([nx,ny])

    return -1
