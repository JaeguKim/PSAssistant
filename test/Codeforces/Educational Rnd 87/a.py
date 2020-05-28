#테스트 케이스중간에 런타임에러가 난경우 - 분모가 영인경우
from math import ceil
t = int(input())
for i in range(t):
    a,b,c,d = map(int,input().split())
    res = 0
    if a<=b:
        res = b
    else:
        if c-d<=0:
            res = -1
        else:
            x = ceil((a-b)/(c-d))
            res = b+c*x
    print(res)
