#33min
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

n,a,b,c = map(int,input().split())
aLoop = int(n/a); bLoop = int(n/b)  # [1] [1]
maxP = -1
for i in range(aLoop+1):
    for j in range(bLoop+1):
        k = (n-i*a-j*b)/c 
        if k.is_integer() and k>=0:
            maxP=max(maxP,i+j+k)
print(int(maxP))