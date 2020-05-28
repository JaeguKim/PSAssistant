#30min
#자신의 생각을 고집하지 말고 모든지점에서 실수할수 있다는 가능성을 열어두자
n,m = map(int,input().split())
f = [int(ch) for ch in input().split()]
f = sorted(f)
res = 2000
for i in range(m-n+1):
    diff = f[i+n-1]-f[i]
    res = min(diff,res)
if m-n == 0:
    res = f[n-1]-f[0]
print(res)
    
