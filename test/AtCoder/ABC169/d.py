#문제를 풀때 너무 조급하기도 해서 행간을 읽지 못했다.
#생각해보면 그렇게 어려운 문제는 아닌데 여러 예외상황을 생각하기가 쉽지 않은거같다.
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

n = inp()

def factoriation(n):
    arr = []
    temp = n
    for i in range(2,int(sqrt(n))+1):
        if temp%i == 0:
            cnt = 0
            while temp%i == 0:
                cnt+=1
                temp //= i
            arr.append([i,cnt])

    if temp != 1:
        arr.append([temp,1])
    if arr==[]:
        arr.append([n,1])
    return arr

fact = factoriation(n)
res = 0
if n==1:
    print(0)
    exit()
for i in range(len(fact)):
    for j in range(1,fact[i][1]+1):
        if n%(fact[i][0]**j) == 0:
            res+=1
            n = n/(fact[i][0]**j)
print(res)