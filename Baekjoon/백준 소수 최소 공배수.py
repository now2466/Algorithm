import math
n = int(input())
nums = list(map(int,input().split()))




prime = []
for x in nums:
    if x==2 or x==3:
        if x not in prime:
            prime.append(x)
    else:
        m = int(math.sqrt(x))+1
        for i in range(2,m):
            if x%i==0:
                break
        else:
            if x not in prime:
                prime.append(x)
answer = 1
for x in prime:
    answer*=x

if answer==1:
    print(-1)
else:
    print(answer)
