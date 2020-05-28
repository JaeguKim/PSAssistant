#최적화 아이디어가 잘 생각이 안나던 문제
def makeTimeIdxList(food_times):
    res = []
    for i in range(len(food_times)):
        res.append([i,food_times[i]])
    res = sorted(res,key=lambda x: x[1])
    return res
    
def solution(food_times, k):
    timeIdxList = makeTimeIdxList(food_times)
    prev = 0
    idx = 0
    isAns = False
    for i in range(len(timeIdxList)):
        totalSubtractCnt = (timeIdxList[i][1]-prev)*(len(timeIdxList)-i)
        if k < totalSubtractCnt:
            idx = i
            isAns = True
            break
        k-=totalSubtractCnt
        prev = timeIdxList[i][1]
    if isAns == False:
        return -1
    newTimeList = sorted(timeIdxList[idx:],key=lambda x: x[0])
    res = newTimeList[k%len(newTimeList)][0]+1
    return res

#거의 같으나 좀더 직관적인 풀이
def solution2(food_times, k):
    food_times_list = []
    totalTime = 0

    for i in range(0, len(food_times)):
        food_times_list.append([i, food_times[i]])
        totalTime+=food_times[i]

    if totalTime <= k:
        return -1

    food_times_list = sorted(food_times_list, key=lambda x:x[1])

    delTime = food_times_list[0][1]*len(food_times_list)
    i=1
    while delTime < k:
        k-=delTime
        delTime = (food_times_list[i][1]-food_times_list[i-1][1])*(len(food_times_list)-i)
        i+=1

    food_times_list = sorted(food_times_list[i-1:], key=lambda x:x[0])
    return food_times_list[k%len(food_times_list)][0]+1

print(solution([3, 1, 2],5))
print(solution([6],7))