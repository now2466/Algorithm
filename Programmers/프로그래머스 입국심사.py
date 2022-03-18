n = 6
times = [1,2.3]

def solution(n,times):
    left = 1
    right = max(times)*n

    def check(mid):
        count = 0
        for x in times:
            count+=mid//x
        return count
        
        
    answer = 0
    while left<=right:
        mid = (left+right)//2

        if check(mid)>=n:
            answer = mid
            right = mid-1
            
        else:
            left = mid+1

    return answer
