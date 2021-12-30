def solution(n):
    pibo = [0]*(n+1)
    pibo[0]=0
    pibo[1]=1
    i=2
    while i<=n:
        pibo[i] = pibo[i-1]+pibo[i-2]
        i+=1
    

    return pibo[n]


print(solution(3))
