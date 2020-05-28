#9min 35s
from math import ceil
n,x,y = [int(ch) for ch in input().split(' ')]
ans = (ceil(y*n/100) - x)
print('0') if ans < 0 else print(ans)