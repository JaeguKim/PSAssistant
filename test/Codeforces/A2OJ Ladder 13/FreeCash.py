#11min
import sys
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
hash = {}
res = -1
for i in range(n):
    h,m = map(int,input().split())
    min = h*60+m
    if min not in hash:
        hash[min] = 1
    else:
        hash[min]+=1
    res = max(hash[min],res)
print(res)
    