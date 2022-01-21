from collections import deque


def solution(n,a,b):
    count=1
    while True:
        count+=1
        
        a=(a+1)//2
        
        b=(b+1)//2

        if a==b:
            break
    return count
