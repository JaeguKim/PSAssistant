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

#27min
n,r,avg = map(int,input().split())
res = 0
array = []
gradeSum = 0
for i in range(n):
    a,b = map(int,input().split())
    array.append([a,b])
    gradeSum += a
array = sorted(array,key=lambda x:x[1])
gradeAvg = gradeSum/n
if gradeAvg<avg:
    x = n*avg-gradeSum
    for i in range(len(array)):
        res += min(r-array[i][0],x)*array[i][1]
        x-=min(r-array[i][0],x)
        if x<=0:
            break
print(res)
