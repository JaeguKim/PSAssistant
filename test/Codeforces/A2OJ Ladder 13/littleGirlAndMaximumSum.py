#idea 필요한 문제
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

n,q = map(int,input().split())
nums = list(map(int,input().split()))
nums = sorted(nums,reverse=True)
cntStartFromIdx = [0]*(n+1)
cntEndFromIdx = [0]*(n+1)
cnts = [0]*n
for i in range(q):
    start,end = map(int,input().split())
    cntStartFromIdx[start] += 1
    if end+1 <= n:
        cntEndFromIdx[end+1] += 1
accumSum = 0
for i in range(1,n+1):
    accumSum += cntStartFromIdx[i]-cntEndFromIdx[i]
    cnts[i-1] = accumSum
cnts = sorted(cnts,reverse=True)
res = 0
for i in range(n):
    res += nums[i]*cnts[i]
print(res)