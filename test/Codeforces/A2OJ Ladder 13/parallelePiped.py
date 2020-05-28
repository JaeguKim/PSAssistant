#21min
from math import sqrt
x,y,z = map(int,input().split())
a = int(sqrt(x*z/y))
b = int(x/a)
c = int(z/a)
res = int(4*(a+b+c))
print(res)