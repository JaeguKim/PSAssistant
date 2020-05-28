#9min 57sec
n,k = [int(ch) for ch in input().split()]
x = 0
for num in [int(ch) for ch in input().split(' ')]:
    if num+k <= 5:
        x += 1
res = int(x/3)
print(res)

