#11min
n,m = [int(ch) for ch in input().split(' ')]
line = [int(ch) for ch in input().split(' ')]
list = []
for elem in line:
    if elem < 0:
        list.append(-1 * elem)
list = sorted(list,reverse=True)
res = 0
for i in range(min(len(list),m)):
    res+=list[i]
print(res)


