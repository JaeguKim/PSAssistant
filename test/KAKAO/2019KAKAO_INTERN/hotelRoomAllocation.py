import sys
sys.setrecursionlimit(1500)

def findNextRoom(room,roomDict):
    if room not in roomDict:
        roomDict[room] = room+1
        return room
    parent = roomDict[room]
    nextRoom = findNextRoom(parent,roomDict)
    roomDict[room] = nextRoom
    return nextRoom


def solution(k, room_number):
    answer = []
    roomDict = {}
    for room in room_number:
        nextRoom = findNextRoom(room,roomDict)
        answer.append(nextRoom)

    return answer

print(solution(10,[1,3,4,1,3,1]))