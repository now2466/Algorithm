n, m = map(int,input().split())

nums = list(map(int,input().split()))
nums = list(set(nums))
nums.sort()

res = [0]*m
def DFS(level):
    if level == m:
        print(" ".join(map(str,res)))
        return
    else:
        for i in range(len(nums)):
            res[level] = nums[i]
            DFS(level+1)
        
    
DFS(0)


