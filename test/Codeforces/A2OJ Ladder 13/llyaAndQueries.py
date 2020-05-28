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
    
str = input()
n = len(str)
m = int(input())
dp = [0]*(n+1)
for i in range(1,n):
    if str[i-1] == str[i]:
        dp[i+1] = dp[i]+1
    else:
        dp[i+1] = dp[i]
#print(dp)
for i in range(m):
    l,r = map(int,input().split())
    print(dp[r]-dp[l])


    
        






