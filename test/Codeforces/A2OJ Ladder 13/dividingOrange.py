#31m
n,k = map(int,input().split())
totalList = []
for i in range(1,n+1):
    totalList.append(i)
ans = []
idxList = [int(ch) for ch in input().split()]
for i in range(k):
    ans.append([idxList[i]])

for i in range(k):
    for j in range(1,n*k+1):
        if len(ans[i]) == n:
            break
        if j not in idxList:
            ans[i].append(j)
            idxList.append(j)
for item in ans:
    for num in item:
        print(num,end=' ')
    print()
    
