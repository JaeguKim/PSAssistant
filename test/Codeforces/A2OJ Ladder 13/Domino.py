#관찰로 충분히 풀수 있지 않았을까 하는 아쉬움이남는다,여러가지 경우를 나눠가면서 생각해보기

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
numOfDiff = 0
sumX = 0
sumY = 0
for i in range(n):
    x,y = map(int,input().split())
    if (x%2 == 0 and y%2 != 0) or (x%2 != 0 and y%2 == 0):
        numOfDiff += 1
    sumX += x
    sumY += y
if sumX %2 == 0 and sumY %2 == 0:
    print(0)
elif (sumX%2 == 0 and sumY %2 != 0) or (sumX%2 !=0 and sumY%2 == 0):
    print(-1)
elif numOfDiff == 0:
    print(-1)
else:
    print(1)
