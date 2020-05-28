k,n = map(int,input().split())
diff = []
a = list(map(int,input().split()))
for i in range(1,n):
    diff.append(a[i]-a[i-1])
diff.append(k-a[n-1]+a[0])
ans = k-max(diff)
print(ans)