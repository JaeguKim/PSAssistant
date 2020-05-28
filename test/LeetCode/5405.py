def buildArray(target,n):
    numList = []
    for i in range(n):
        numList.append(i+1)
    idx = 0
    res = []
    for i in range(n):
        res.append("Push")
        if numList[i] != target[idx]:
            res.append("Pop")
        else:
            idx+=1
        if idx > len(target)-1:
            break
            
    return res

print(buildArray([1,3],3))
print(buildArray([1,2,3],3))
print(buildArray([1,2],4))
