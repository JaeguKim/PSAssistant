#2min 47sec
n = int(input())
res = 0
for i in range(n):
    line = [int(ch) for ch in input().split()]
    if sum(line) >= 2:
        res+=1
print(res)

