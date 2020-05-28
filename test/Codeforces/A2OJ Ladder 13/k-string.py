#18min
k = int(input())
s = input()
cntDict = {}
for ch in s:
    if ch not in cntDict:
        cntDict[ch] = 1
    else:
        cntDict[ch]+=1

for key in cntDict.keys():
    cnt = cntDict[key]
    if cnt%k != 0:
        print(-1)
        exit()
    else:
        cntDict[key]=int(cntDict[key]/k)
res = []
for i in range(k):
    for key in cntDict.keys():
        for j in range(cntDict[key]):
            res.append(key)
print(''.join(res))
