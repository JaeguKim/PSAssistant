from math import floor

line = [int(ch) for ch in input().split()]
a = line[0]; b = line[1]; n = line[2]
if b <= n:
    x = b-1
else:
    x = n
res = floor(a*x/b) - a*floor(x/b)
print(res)