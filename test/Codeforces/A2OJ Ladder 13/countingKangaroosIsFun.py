#1h
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

n = int(input())
size = []
for i in range(n):
    size.append(int(input()))
if len(size) == 1:
    print('1')
else:
    size = sorted(size)
    leftCur = 0
    right=int(n/2)
    rightCur = right
    res = 0
    while leftCur<right and rightCur<n:
        leftVal = size[leftCur]; rightVal = size[rightCur];
        if leftVal*2 <= rightVal:
            res+=1
            leftCur+=1; rightCur+=1
        else:
            rightCur+=1
    print(n-res)
