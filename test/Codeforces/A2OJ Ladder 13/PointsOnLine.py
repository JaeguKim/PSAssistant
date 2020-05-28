n,d = map(int,input().split())
a = list(map(int,input().split()))
res = 0
left = 0
for right in range(n):
    while a[right]-a[left] > d:
        left+=1
    x = right-left
    res += int(x*(x-1)/2)
print(res)


