def convertMusicToList(musicStr):
    musicStr = musicStr.replace('C#','c')
    musicStr = musicStr.replace('D#','d')
    musicStr = musicStr.replace('F#','f')
    musicStr = musicStr.replace('G#','g')
    musicStr = musicStr.replace('A#','a')
    print(musicStr)
    return musicStr

def getMusicInfo(time,cords):
    convCords = convertMusicToList(cords)
    divideResult = int(time/len(convCords))
    residue = time%len(convCords)
    resultStr = ''
    for i in range(divideResult):
        resultStr += convCords
    for i in range(residue):
        resultStr += convCords[i]
    return resultStr

def getTimeTuple(time):
    arr = time.split(':')
    hour = int(arr[0].lstrip())
    min = int(arr[1].lstrip())
    return (hour,min)

def getTimeInterval(start,end):
    startTuple = getTimeTuple(start)
    endTuple = getTimeTuple(end)
    result = endTuple[0]*60+endTuple[1] - (startTuple[0]*60 + startTuple[1])
    return result

def solution(m, musicinfos):
    convertedM = convertMusicToList(m)
    answerArr = []
    for str in musicinfos:
        arr = str.split(',')
        timeInterval = getTimeInterval(arr[0],arr[1])
        musicStr = getMusicInfo(timeInterval,arr[3])
        print(musicStr)
        if convertedM in musicStr:
            answerArr.append([timeInterval,arr[2]])
    answer = ''
    if len(answerArr) == 0:
        answer = '(None)'
    else:
        sortedArr = sorted(answerArr,key=lambda x: x[0],reverse=True)
        answer = sortedArr[0][1]
    return answer

#print(solution("ABCDEFG",["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
#print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))