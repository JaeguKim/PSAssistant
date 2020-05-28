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

n,k = map(int,input().split())
h = list(map(int,input().split()))
sumAry = [0]*n
sumAry[0] = h[0]
for i in range(1,n):
    sumAry[i] = sumAry[i-1]+h[i]
minSum = sumAry[k-1]
res = 1
for i in range(1,n):
    if i+k-1 > n-1:
        break
    else:
        intervalSum = sumAry[i+k-1]-sumAry[i-1]
        if intervalSum < minSum:
            res = i+1
            minSum = min(intervalSum,minSum)
print(res)

