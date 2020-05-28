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

t=inp()
for i in range(t):
    n=inp()
    a = inlt()
    a = sorted(a)
    cnt=1
    res=1
    for i in range(len(a)):
        if cnt>=a[i]:
            res=cnt+1
        cnt+=1
    print(res)
