import sys
from collections import deque
n, m = map(int,input().split())

s = [0,0]
board = []

for _ in range(n):
    board.append(list(map(int,input())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]
queue = deque()


visited = [[0] * m for _ in range(n)]

#x좌표, y좌표, 걸어온 칸 수를 넣을거임
queue.append([0,0])
visited[0][0]=1
while queue:
    x, y = queue.popleft()
    board[x][y]=0
    if x==n-1 and y ==m-1:
        print(visited[x][y])
        break

    for k in range(4):
        nx = x+dx[k]
        ny = y+dy[k]
        if 0<=nx<n and 0<=ny<m:
            if visited[nx][ny]==0 and board[nx][ny]==1:
                visited[nx][ny] = visited[x][y]+1
                queue.append([nx,ny])
