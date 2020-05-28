#planning : 15m 50s
#coding : 45m
#total : 1h
import collections

def convertStr(num,n):
    dict = {10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
    if num<n:
        if num>=10:
            return dict[num]
        else:
            return str(num)
    result = ''
    new = num
    while new >= n:
        if new%n >= 10:
            result = dict[new%n] + result
        else:
            result = str(new%n) + result
        new = int(new/n)
    if new>=10:
        new = dict[new]
    result = str(new) + result
    return result




def solution(n, t, m, p):
    num = 0
    result = ''
    while (True):
        result += convertStr(num,n)
        if len(result) >= m*t:
            break
        num+=1
    answer = ''
    for i in range(t):
        answer += result[i*m + p - 1]
    return answer

print(solution(2,4,2,1))