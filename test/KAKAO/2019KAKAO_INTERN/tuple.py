#understanding : 2m34s
#coding : 51m 30s
#total : 53m 30s
def solution(s):
    list = []
    lists = []
    isNumStart = False
    startIdx = 0
    endIdx = 0
    for i in range(len(s)):
        if  s[i].isnumeric():
            if isNumStart == False:
                startIdx = i
                endIdx = i
                isNumStart = True
            else:
                endIdx = i
        elif s[i] == ',' and s[i-1].isnumeric():
            list.append(int(s[startIdx:endIdx+1]))
            isNumStart = False
        elif s[i] == '}' and s[i-1].isnumeric():
            list.append(int(s[startIdx:endIdx+1]))
            lists.append(list)
            list = []
            isNumStart = False
        lists.sort(key=len)
    result = []
    for list in lists:
        for num in list:
            if num not in result:
                result.append(num)
    return result

def solution2(s):
    s = Counter(re.findall('\d+', s))
    print(s)
    return list(map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)]))

import re
from collections import Counter

s1 = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
s2 = "{{1,2,3},{2,1},{1,2,4,3},{2}}"
solution(s1)
solution(s2)
solution2(s1)