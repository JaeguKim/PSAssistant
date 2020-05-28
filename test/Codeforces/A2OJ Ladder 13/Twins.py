#12min
n = int(input())
ary = list(map(int,input().split()))
sumA = 0
sumB = 0
res = 0
if n == 1:
    print(1)
    exit()
ary = sorted(ary)
while True:
    sumA += ary[-1]
    ary = ary[:-1]
    sumB = sum(ary)
    res+=1
    if sumA > sumB:
        break
print(res)