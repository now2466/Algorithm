def solution(w,h):
    import math

    a = min(w,h)
    b = max(w,h)
    if a!=b:
        d = (b//a)+1
    else:
        d = (b//a)

    return a*(b-d)


print(solution(8,12))
