p = [3, 30, 34, 5, 9]
def solution(p):
    p.sort(key = lambda x:str(x)*3,reverse=True)

    answer = ""
    for x in p:
        answer+=str(x)

    answer = str(int(answer))
    return answer
print(solution(p))
