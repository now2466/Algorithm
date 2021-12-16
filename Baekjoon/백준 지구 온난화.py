n, m = map(int,input().split())

maps = []

for _ in range(n):
    maps.append(list(map(str,input())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]
ch = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if maps[i][j]=='X':
            count = 0
            for k in range(4):
                x = i+dx[k]
                y = j+dy[k]
                if (not 0<=x<n) or (not 0<=y<m):
                    count+=1
                elif maps[x][y]=='.':
                    count+=1
            if count>=3:
                ch[i][j]=1

for i in range(n):
    for j in range(m):
        if ch[i][j]==1:
            maps[i][j]='.'
            
first_row = 10
first_col = 10
last_row = 0
last_col = 0

for i in range(n):
    for j in range(m):
        if maps[i][j]=='X':
            if i<first_row:
                first_row=i
            if i>last_row:
                last_row = i
            if j<first_col:
                first_col = j
            if j>last_col:
                last_col = j
for i in range(first_row,last_row+1):
    for j in range(first_col, last_col+1):
        print(maps[i][j],end="")
    print()
                    
