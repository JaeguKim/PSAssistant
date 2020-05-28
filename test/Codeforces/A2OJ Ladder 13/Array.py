#idea는 찾았지만 구현이 생각보다 까다로웠다.
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

n,k = map(int,input().split())
a = list(map(int,input().split()))
l=0;r=0;
res = [-1,-1]
hash = {}
minLen = n+1
end = False
while True:
    if len(hash) == k:
        length = r-l
        if length < minLen:    
            res[0] = l+1
            res[1] = r
            minLen = length
        hash[a[l]] -= 1
        if hash[a[l]] == 0:
            hash.pop(a[l],None)
        l+=1
    else:
        if end:
            break
        key = a[r]
        if key not in hash:
            hash[key] = 1
        else:
            hash[key] += 1
        if r < len(a):
            r+=1
        if r >= len(a):
            end = True
print('{} {}'.format(res[0],res[1]))