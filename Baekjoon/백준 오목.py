import sys
pan = [[0]*21 for _ in range(21)]

board = []

for _ in range(19):
    x = list(map(int,input().split()))
    board.append(x)

for i in range(19):
    for j in range(19):
        pan[i+1][j+1]=board[i][j]

dx = [-1,0,1,1]
dy = [1,1,1,0]

for i in range(21):
    for j in range(21):
        if pan[i][j]!=0:
            for k in range(4):
                bx = i-dx[k]
                by = j - dy[k]
                if 0<=bx<21 and 0<=by<21 and pan[bx][by]!=pan[i][j]:
                    x = i+dx[k]
                    y = j+dy[k]
                    count=1
                    while 0<=x<21 and 0<=y<21 and pan[x][y]==pan[i][j]:
                        x = x+dx[k]
                        y = y+dy[k]
                        count+=1
                    if count==5:
                        print(pan[i][j])
                        print(i,j)
                        sys.exit(0)
                        

print(0)
    
                    
            
