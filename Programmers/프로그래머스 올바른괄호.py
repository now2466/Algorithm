def solution(s):
    stack = []

    for x in s:
        if x =="(":
            stack.append(x)
        else:
            if len(stack):
                stack.pop()
            else:
                return False
    if len(stack):
        return False
    else:
        return True
