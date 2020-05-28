#21min
#신중하게 생각하고 정확도에 더 신경을 쓰자
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
bits = list(map(int,input().split()))
res=-1
for i in range(n):
    for j in range(i,n):
        temp = bits.copy()
        for k in range(i,j+1):
            temp[k] = 1-temp[k]
        res = max(temp.count(1),res)
print(res)        