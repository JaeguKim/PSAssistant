#5min
n1 = [ch for ch in input()]
n2 = [ch for ch in input()]
res = ''
for i in range(len(n1)):
    if n1[i] == n2[i]:
        res += '0'
    else:
        res += '1'
print(res)