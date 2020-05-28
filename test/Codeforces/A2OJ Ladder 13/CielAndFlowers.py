#관찰력이 필요한 문제
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


r,g,b = map(int,input().split())
res = min(min(r,g),b)
for i in range(0,3):
    newR = r-i if r-i>=0 else -1
    newG = g-i if g-i>=0 else -1
    newB = b-i if b-i>=0 else -1
    if newR == -1 or newG == -1 or newB == -1:
        continue
    res = max(res,int(newR/3)+int(newG/3)+int(newB/3)+i)
print(res)