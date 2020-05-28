#1hour 03min
#list는 object 타입임을 유의하자
import collections

def makeMatchList(user_id, banned_id):
    res = []
    for b_id in banned_id:
        list = []
        for u_id in user_id:
            if len(u_id) == len(b_id):
                isOk = True
                for i in range(len(b_id)):
                    if b_id[i] != '*' and b_id[i] != u_id[i]:
                        isOk = False
                if isOk:
                    list.append(u_id)
        res.append(list)
    return res

def check(curList,res):
    if len(res) == 0:
        return True
    for resList in res:
        if collections.Counter(curList) == collections.Counter(resList):
            return False
    return True

def recursion(curIdx,curList,matchList,n,res):
    if curIdx > n-1:
        if check(curList,res):
            res.append(curList.copy())
        return
    for item in matchList[curIdx]:
        if item in curList:
            continue
        curList.append(item)
        recursion(curIdx+1,curList,matchList,n,res)
        curList.remove(item)

def solution(user_id, banned_id):
    matchList = makeMatchList(user_id,banned_id)
    res = []
    recursion(0,[],matchList,len(banned_id),res)
    ans = len(res)
    return ans


#print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))
#print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))