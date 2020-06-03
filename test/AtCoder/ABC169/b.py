#TIME : 
import sys
from math import sqrt
input = sys.stdin.readline

def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))

MAX = 10**18
n = inp()
a = inlt()
if 0 in a:
    print(0)
    exit()
res = 1
for num in a:
    res*=num
    if res > MAX:
        print(-1)
        exit()
print(res)