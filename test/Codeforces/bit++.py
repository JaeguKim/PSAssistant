#5min
n = int(input())
res = 0
for i in range(n):
    line = input()
    if '++' in line:
        res += 1
    elif '--' in line:
        res -= 1
print(res)
