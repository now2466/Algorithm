def solution(record):
    record_dict = dict()

    record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

    for mes in record:
        x = mes.split()
        if x[0]=='Enter':
            record_dict[x[1]]=x[2]
        elif x[0]=='Change':
            record_dict[x[1]]=x[2]

    answer = []

    for mes in record:
        x = mes.split()
        if x[0]=='Enter':
            answer.append(record_dict[x[1]]+'님이 들어왔습니다.')
        elif x[0]=='Leave':
            answer.append(record_dict[x[1]]+'님이 나갔습니다.')

    return answer
