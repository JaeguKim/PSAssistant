#18min
n,m = [int(num) for num in input().split(' ')]
sum = 0
cur = 0
while sum <= m:
    cur += 1
    sum += cur
    if cur == n and sum <= m:
        cur = 0
    
sum -= cur
print(m-sum)
