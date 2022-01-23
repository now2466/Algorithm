import collections

phone_book = ["12","123","1235","567","88"]
def solution(phone_book):
    nH = collections.defaultdict(int)
    for num in phone_book:
        temp = ''
        for x in num:
            temp+=x
            nH[temp]+=1

    for num in phone_book:
        if nH[num]>1:
            return False
    else:
        return True
print(solution(phone_book))
