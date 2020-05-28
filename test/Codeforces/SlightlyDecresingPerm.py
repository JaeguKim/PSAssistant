#26min
n,k = [int(ch) for ch in input().split(' ')]
input = [i+1 for i in range(n)]
idx = n-1-k
left = input[:n-1-k]
right = input[n-1-k:]
res = left + sorted(right,reverse=True)
ans = ''
for num in res:
    print(num,end=' ')


