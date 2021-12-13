n = int(input())

def isvalid(x):
    import math
    if x<=1:
        return False
    for i in range(2,int(math.sqrt(x))+1):
        if x%i==0:
            return False
    return True

for _ in range(n):
    x = int(input())
    while True:
        if isvalid(x):
            print(x)
            break
        x+=1
