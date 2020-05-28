def getRonudValue(num):
    return round(num,3)

def solution(lines):
    intervalList = []
    inputInterval = []
    for line in lines:
        list = line.split(' ')
        timeAry = list[1].split(':')
        hourPlusSec = float(int(timeAry[0])*3600+int(timeAry[1])*60)
        endTime = float(timeAry[2].lstrip('0'))+hourPlusSec
        interval = float(list[2].replace('s',''))
        precision = 0.001
        startTime = endTime-interval+precision
        intervalList.append([getRonudValue(startTime),getRonudValue(startTime+1-precision)])
        intervalList.append([getRonudValue(endTime),getRonudValue(endTime+1-precision)])
        inputInterval.append([getRonudValue(startTime),getRonudValue(endTime)])
    answer = 0
    for interval in intervalList:
        count = 0
        for input in inputInterval:
            if input[0] <= interval[1] and input[1]>=interval[0]:
                count += 1
        answer = max(count,answer)
    return answer

#print(solution(["2016-09-15 01:00:04.001 2.0s","2016-09-15 01:00:07.000 2s"
#]))
print(solution(["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"]))


