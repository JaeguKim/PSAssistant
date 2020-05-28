#13min 
#시간복잡도에 대해서 신경쓰지못해서 한번 fail
import math

y,k,n = map(int,input().split())
res = []

start = math.ceil((1+y)/k)
end = math.floor(n/k)
for i in range(start,end+1):
    res.append(i*k-y)

if len(res) == 0:
    print('-1')
else:
    for num in res:
        print(num,end=' ')
