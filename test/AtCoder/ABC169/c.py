
#TIME : 
#when calculating decimal numbers in python, we should use Decimal library. float has precision error becasue it represents with binary format.
#Use __truncate__ when getting integer part of Decimal object. Don't use int().
import sys
from math import sqrt
from decimal import Decimal

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

AB = input().split()
a = Decimal(AB[0])
b = Decimal(AB[1])
res = (a*b).__trunc__()
print(res)