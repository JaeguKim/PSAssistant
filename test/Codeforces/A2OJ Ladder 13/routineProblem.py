import sys
from math import sqrt
from fractions import Fraction
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

a,b,c,d = invr()
newW = c*b/d
newH = d*a/c
res = '{}/{}'.format(0,1)
if newW < a:
    res = str(Fraction((a-newW)/a).limit_denominator())
elif newH < b:
    res = str(Fraction((b-newH)/b).limit_denominator())
print(res)