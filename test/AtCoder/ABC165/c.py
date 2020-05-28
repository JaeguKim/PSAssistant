#48min 41sec
#완전탐색으로 통과가 안될거라고 생각하고 넘어간문제, 사실은 완탐으로 가능
def recursion(n,m,curList,res):
    if len(curList) == n:
        res.append(curList.copy())
        return

    for i in range(1,m+1):
        if len(curList) > 0 and i < curList[-1]:
            continue
        curList.append(i)
        recursion(n,m,curList,res)
        curList.remove(curList[-1])

def makeSequenceList(n,m):
    res = []
    recursion(n,m,[],res)
    return res

n,m,q = map(int,input().split())
quadList = []
for i in range(q):
    quad = [int(ch) for ch in input().split()]
    quadList.append(quad)
seqList = makeSequenceList(n,m)
ans = -1
for seq in seqList:
    sum = 0
    for quad in quadList:
        if seq[quad[1]-1] - seq[quad[0]-1] == quad[2]:
            sum += quad[3]
    ans = max(sum,ans)
print(ans)
