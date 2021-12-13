import sys
n = int(input())


board = [[]for _ in range(n)]
for i in range(n):
    temp = str(input())
    for j in range(n):
        board[i].append(temp[j])

dx = [1,-1,0,0]
dy = [0,0,-1,1]
answer = 0


#check
for i in range(n):
    for j in range(n):
        for k in range(4):
            a = i+dx[k]
            b = j+dy[k]
            flag = True
            if 0<=a<n and 0<=b<n and board[i][j]!=board[a][b]:
                flag=False
                temp = board[a][b]
                board[a][b]=board[i][j]
                board[i][j]=temp
            for k in range(4):
                x = i+dx[k]
                y = j+dy[k]
                count = 1
                while 0<=x<n and 0<=y<n and board[x][y]==board[i][j]:
                    count+=1
                    x+=dx[k]
                    y+=dy[k]
                x = i-dx[k]
                y = j-dy[k]
                while 0<=x<n and 0<=y<n and board[x][y]==board[i][j]:
                    count+=1
                    x-=dx[k]
                    y-=dy[k]
                if count>answer:
                    answer=count
            if flag==False:
                temp = board[a][b]
                board[a][b]=board[i][j]
                board[i][j]=temp

print(answer)
