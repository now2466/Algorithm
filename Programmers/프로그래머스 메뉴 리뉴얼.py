

orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]	
course = [2,3,4]
def solution(orders,course):
    import collections


    def DFS(level,s):
        if level==n:
            temp = ''.join(sorted(res))
            ans[temp]+=1
                
        else:
            for i in range(s,len(order)):
                if ch[i]==0:
                    ch[i]=1
                    res[level]=order[i]
                    DFS(level+1,i)
                    ch[i]=0
    answer = []
    for n in course:
        ans = collections.defaultdict(int)
        for order in orders:
            ch=[0]*len(order)
            res = [0]*n
            DFS(0,0)
        for key, value in ans.items():
            if value>=2 and value==max(ans.values()):
                answer.append(key)


    answer.sort()
    return answer
print(solution(orders,course))
print(solution(["XYZ", "XWY", "WXA"],[2,3,4]))
