#1h 04, 완전히 잘못된 접근으로 시간지체
n,m = map(int,input().split())
a = list(map(int,input().split()))
res = a[0]-1
for i in range(len(a)-1):
    if a[i] < a[i+1]:
        res += a[i+1]-a[i]
    elif a[i] > a[i+1]:
        res += a[i+1]-a[i]+n
print(res)
    
        


