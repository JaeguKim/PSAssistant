#plan : 8m 52s
#coding : 52m
#total : 1h

def solution(msg):
    dict = {}
    answer = []
    a = ord('A')
    b = ord('Z')
    idx = 1
    for i in range(a,b+1):
        dict[chr(i)] = idx
        idx+=1
    startIdx = 0
    for i in range(len(msg)):
        if i != startIdx:
            continue
        str = msg[i]
        indexNum = dict[msg[i]]
        for j in range(i+1,len(msg)):
            str += msg[j]
            if str in dict:
                indexNum = dict[str]
                startIdx = i+len(str)
            else:
                dict[str] = idx
                idx+=1
                startIdx = i+len(str)-1
                break
        answer.append(indexNum)
    
    return answer

print(solution('KAKAO'))
print(solution('TOBEORNOTTOBEORTOBEORNOT'))