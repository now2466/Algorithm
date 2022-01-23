def solution(numbers,target):
    global answer
    answer = 0
    n = len(numbers)
    def DFS(level,s):
        global answer
        if level == n:
            if s == target :
                answer+=1
        else:
            DFS(level+1,s-numbers[level])
            DFS(level+1,s+numbers[level])
    DFS(0,0)

    return answer
print(solution([1,1,1,1,1],3))
