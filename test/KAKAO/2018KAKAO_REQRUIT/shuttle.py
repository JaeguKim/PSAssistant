def getMin(time):
    arr = time.split(':')
    hour = int(arr[0])*60
    min = int(arr[1])
    return hour+min

def getTimeStr(min):
    hour = int(min/60)
    newSec = int(min%60)
    if len(str(hour)) == 1:
        hour = '0'+str(hour)
    if len(str(newSec)) == 1:
        newSec = '0'+str(newSec)
    return str(hour)+':'+str(newSec)

def solution(n, t, m, timetable):
    answer = ''
    arriveTimeList = []
    for i in range(len(timetable)):
        timeInSec = getMin(timetable[i])
        arriveTimeList.append(timeInSec)
    
    arriveTimeList = sorted(arriveTimeList)
    shuttleTime = 540
    idx = 0
    res = 0
    for k in range(n):
        full = m
        for i in range(idx,len(arriveTimeList)):
            if arriveTimeList[i] <= shuttleTime:
                idx+=1
                full-=1
                if full == 0:
                    break
        if k+1 == n:
            if full == 0:
                res = arriveTimeList[idx-1]-1
            else:
                res = shuttleTime
        shuttleTime += t
        if shuttleTime >= 60*24:
            break
    
    answer = getTimeStr(res)
    return answer

#print(solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]))
#print(solution(	2, 10, 2, ["09:10", "09:09", "08:00"]))
print(solution(2, 1, 2, ["09:00", "09:00", "09:00", "09:00"]))