import sys
from math import sqrt
from itertools import combinations
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
res = 0
if n<3:
    res=n
elif n%2 != 0:
    res = n*(n-1)*(n-2)
elif n%3==0:
    res = (n-1)*(n-2)*(n-3)
else:
    res = n*(n-1)*(n-3)
print(res)
           
