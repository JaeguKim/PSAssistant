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

#TLE
'''
def getVal(x,y):
    num = 1
    for i in range(y):
        num+=i
    for i in range(y+1,x+y):
        num+=i
    return num

def solve(hash,curX,curY,endX,endY,val):
    val += getVal(curX,curY)
    print('{} {} {} {}'.format(curX,curY,endX,endY))
    if curX == endX and curY == endY:
        hash[val] = 0
        return
    elif curX > endX or curY > endY:
        return
    
    solve(hash,curX+1,curY,endX,endY,val)
    solve(hash,curX,curY+1,endX,endY,val)
'''

t = inp()
for i in range(t):
    x1,y1,x2,y2 = invr()
    no_D = x2-x1
    no_R = y2-y1
    res = no_D*no_R+1
    print(res)