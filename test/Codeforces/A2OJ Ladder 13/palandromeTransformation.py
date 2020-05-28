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

n,p = map(int,input().split())
line = input().rstrip('\n')
if p > int(len(line)/2):
    line = line[::-1]
    p = n-p+1
l = n; r = -1
for i in range(0,int(n/2)):
    if line[i] != line[n-1-i]:
        l = min(l,i)
        r = max(r,i)
res = 0
if l == n and r == -1:
    res= 0
else:
    for i in range(l,r+1):
        case1 = abs(ord(line[n-1-i])-ord(line[i]))
        case2 = 26 - case1
        num = min(case1,case2)
        res+=num
    res += min(abs(p-1-l),abs(p-1-r)) + r-l
print(res)
