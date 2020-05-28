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

modulo = 1000000007
n,k = map(int,input().split())
dp = [[0]*(n+1) for i in range(k+1)]
for i in range(1,n+1):
    dp[1][i] = 1
for i in range(2,k+1):
    for j in range(1,n+1):
        for z in range(j,n+1,j):
            dp[i][z] += dp[i-1][j]%modulo
res = 0
for i in range(1,n+1):
    res = (res+dp[k][i])%modulo
print(res)