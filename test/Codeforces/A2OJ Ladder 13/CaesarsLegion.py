import sys
from math import sqrt
import math
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

limit_f = 0; limit_h = 0
mod = 100000000
dp = [[[[ -1 for i in range(11)] for j in range(11)] for k in range(101)] for l in range(101)]
def solve(f,h,k1,k2):
    x=0;y=0
    if f+h==0:
        return 1
    
    if dp[f][h][k1][k2] != -1:
        return dp[f][h][k1][k2]

    #insert f
    if f>0 and k1>0:
        x = solve(f-1,h,k1-1,limit_h)

    #insert h
    if h>0 and k2>0:
        y = solve(f,h-1,limit_f,k2-1)

    dp[f][h][k1][k2] = (x+y)%mod
    return dp[f][h][k1][k2]

n1,n2,limit_f,limit_h = map(int,input().split())
res = solve(n1,n2,limit_f,limit_h)
print(res)