def solution(s):
    answer = ""

    for i in range(len(s)):
        if i==0:
            answer+=s[i].upper()
        elif i>0:
            if s[i-1]==' ':
                answer+=s[i].upper()
            else:
                answer+=s[i].lower()
    return answer

print(solution(" hello world"))
