#res에 index를 대상으로 중복검사를 해야하는데, dist[idx] 값을 대상으로 검사해서 해맸다
def solution(n, weak, dist):
    weakList = getWeakList(n,weak)
    minDepth = -1
    for depth in range(1,len(dist)+1):
        res = []
        if recursion(0,depth,dist,weakList,res) == True:
            minDepth = depth
            break
    if minDepth == -1:
        return -1
    return minDepth

def recursion(curDepth,depth,dist,weakList,res):
    if curDepth == depth:
        if check(res,dist,weakList) == True:
            return True
        else:
            return False

    for i in range(len(dist)):
        if i not in res:
            res.append(i)
            if recursion(curDepth+1,depth,dist,weakList,res) == True:
                return True
            res.remove(i)

    return False

def getWeakList(n,weak):
    res = []
    length = len(weak)
    for i in range(len(weak)):
        dist = [0] * length
        idx = 0
        for j in range(len(weak)):
            if j+i > length-1:
                dist[idx] = weak[(j+i)%length] + n
            else:
                dist[idx] = weak[j+i]
            idx+=1
        res.append(dist)
    return res

def isFinish(visit):
    for elem in visit:
        if elem == False:
            return False
    return True

def check(result,dist,weakList):
    num = len(result)
 
    for weak in weakList:
        idx = 0
        start = 0
        visit = [False] * len(weakList)
        while idx != num:
            i = start
            value = dist[result[idx]]
            idx+=1
            for j in range(start,len(weak)):
                if not(weak[i] <= weak[j] and weak[j] <= weak[i]+value):
                    break
                visit[j] = True
                start+=1
        if isFinish(visit):
            return True
    return False

#print(solution(12,[1, 5, 6, 10],[1, 2, 3, 4]))
#print(solution(12,[1, 3, 4, 9, 10],[3, 5, 7]))
#print(solution(50, [1, 5, 10, 12, 22, 25], [3,4,6]))
print(solution(50, [1, 5, 10, 12, 22, 25], [4, 3, 2, 1]))
#print(solution(50,[1],[6]))

