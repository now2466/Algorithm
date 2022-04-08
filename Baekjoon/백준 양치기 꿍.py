import sys
sys.setrecursionlimit(1000000)
n, m = map(int,sys.stdin.readline().split())

field = [[] for _ in range(n)]
for i in range(n):
    temp = input()
    for k in range(m):
        field[i].append(temp[k])

dx = [-1,0,1,0]
dy = [0,-1,0,1]

def DFS(x,y):
    global wolf
    global sheep
    if field[x][y]=="v":
                    wolf+=1
    elif field[x][y]=="k":
        sheep+=1

    field[x][y]="#"
    
    for k in range(4):
        nx = x+dx[k]
        ny = y+dy[k]
        if 0<=nx<n and 0<=ny<m:
            if field[nx][ny]!="#":
                DFS(nx,ny)
surv_wolf=0
surv_sheep=0
for i in range(n):
    for j in range(m):
        wolf=0
        sheep=0
        if field[i][j]!="#":
            DFS(i,j)
        if wolf<sheep:
            surv_sheep+=sheep
        else:
            surv_wolf+=wolf

print(surv_sheep, surv_wolf)











        
