#planning : 10m 52s
#coding : 36m
#total : 46m 30s

def solution(record):
    list1 = []
    list2 = []
    dict = {}
    for str in record:
        ary = str.split(' ')
        list1.append(ary[0])
        list2.append(ary[1])
        if ary[0] == 'Enter' or ary[0] == 'Change':
            dict[ary[1]] = ary[2]
       
    answer = []
    for i in range(len(list1)):
        if list1[i] == 'Change':
            continue
        result = ''
        op = ''
        if list1[i] == "Enter":
            op = "들어왔습니다."
        elif list1[i] == "Leave":
            op = "나갔습니다."
        result = dict[list2[i]] + '님이 ' + op
        answer.append(result)
    return answer

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))