#planning : 7m 44
#coding : 
#total : 20min+

import re

def solution(files):
    answer = []
    #head - number - tail로 나누는 re
    p = re.compile("([a-z\-\s]+)([0-9]+)(.*)")
    s_list = []

    #head, number, 원본으로 저장
    for temp in files:
        g = p.search(temp.lower())
        head = g.group(1)
        num = int(g.group(2))
        s_list.append((head,num,temp))

    #정렬한 후 list 출력
    s_list = sorted(s_list, key=lambda x:(x[0],x[1]))
    for i in s_list:
        answer.append(i[2])

    return answer

files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
print(solution(files))
files = ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
print(solution(files))

