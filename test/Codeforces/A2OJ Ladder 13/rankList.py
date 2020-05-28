#20min
n,k = map(int,input().split())
pairs = []
for i in range(n):
    p,t = map(int,input().split())
    pairs.append([p,t])
pairs = sorted(pairs,key=lambda x: x[1])
pairs = sorted(pairs,key=lambda x: x[0],reverse=True)
cnt = {}
for pair in pairs:
    key = (pair[0],pair[1])
    if key not in cnt:
        cnt[key] = 1
    else:
        cnt[key] += 1
key = (pairs[k-1][0],pairs[k-1][1])
res = cnt[key]
print(res)

