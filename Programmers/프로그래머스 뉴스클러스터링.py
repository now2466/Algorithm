import collections
def solution(str1,str2):
    set1 = collections.defaultdict(int)
    set2 = collections.defaultdict(int)
    str1 = str1.lower()
    str2 = str2.lower()
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            set1[str1[i]+str1[i+1]]+=1


    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            set2[str2[i]+str2[i+1]]+=1
    inter = 0
    union = 0
    for x in (set(set1)|set(set2)):
        union += max(set1[x],set2[x])
    for x in (set(set1)&set(set2)):
        inter += min(set1[x],set2[x])

    if union == 0:
        return 65536
    else:
        return int(inter/union*65536)

