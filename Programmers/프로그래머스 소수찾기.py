import math
numbers = '17'


def solution(numbers):
    ch = [0]*len(numbers)
    answer = []
    def DFS(level,s):
        if level>0:
            temp = int(s)
            if temp>1 and temp not in answer:
                answer.append(temp)
            
        for i in range(len(numbers)):
            if ch[i]==0:
                ch[i]=1
                DFS(level+1,s+numbers[i])
                ch[i]=0

        
    DFS(0,'')

    count = 0
    for x in answer:
        if x >2:
            for i in range(2,int(math.sqrt(x))+1):
                if x%i==0:
                    break
            else:
                count+=1
        elif x==2:
            count+=1
    return count
