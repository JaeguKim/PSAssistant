#11min 55s
n = int(input())
dict = {}
arr = [int(ch) for ch in input().split()]
for i in range(n):
    dict[arr[i]] = 1
ans = 0
for i in range(1,n+1):
    if i not in dict.keys():
        ans+=1
print(ans)