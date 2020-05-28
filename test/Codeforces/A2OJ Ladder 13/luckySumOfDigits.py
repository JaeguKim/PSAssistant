#알고리즘은 거의 맞았으나, 사소한 함수들을 최적화해야 accept되는 문제
import sys
def printMin(a,b):
    for i in range(b):
        print('4',end='')
    for i in range(a):
        print('7',end='')

n = int(input())
a = 0
find = False
aCnt = -1
bCnt = -1
m=sys.maxsize
prev = sys.maxsize
while 7*a <= n:
    if (n-7*a)%4 == 0:
        b = int((n-7*a)/4)
        if a+b < m:
            aCnt = a
            bCnt = b
            m = a+b
    a+=1
if aCnt == -1 or bCnt == -1:
    print('-1')
else:
    printMin(aCnt,bCnt)
