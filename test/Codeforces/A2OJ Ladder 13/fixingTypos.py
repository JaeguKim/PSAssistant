import sys
from math import sqrt
input = sys.stdin.readline

############ ---- Input Functions ---- ############
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))

s=input()
length = len(s)
leftIdx = 0
res = ''
_list = []
while leftIdx < length:
    cnt = 1
    ch = s[leftIdx]
    for i in range(leftIdx+1,length):
        if ch == s[i]:
            cnt+=1
        else:
            break
    leftIdx+=cnt
    _list.append([ch,cnt])
for pair in _list:
    if pair[1]>=3:
        pair[1]=2
for i in range(len(_list)-1):
    if _list[i][1]==2:
        _list[i+1][1] = 1
for pair in _list:
    for i in range(pair[1]):
        print(pair[0],end='')