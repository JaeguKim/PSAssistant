from itertools import combinations
#확률공부가 어느정도 되어있으면 간단한 풀이가 가능
m,n = map(int,input().split())
prev = 0
res = 0
for i in range(1,m+1):
    cur = pow(i/m,n)
    res += i*(cur-prev)
    prev = cur
print(res)
