#2hour 15m
def getLockWithPadding(lockMat,M,N):
    length = N+2*M
    newMat = []
    for i in range(length):
        newMat.append([])
        for j in range(length):
            newMat[i].append(0)
    offset = M
    for i in range(N):
        for j in range(N):
            newMat[i+offset][j+offset] = lockMat[i][j]

    return newMat

def getKeyWithPadding(key,M,N,startRow,startCol):
    length = N+2*M
    newMat = []
    for i in range(length):
        newMat.append([])
        for j in range(length):
            newMat[i].append(0)
    for i in range(M):
        for j in range(M):
            newMat[i+startRow][j+startCol] = key[i][j]
    return newMat

def check(keyWithPadding,lockWithPadding,M,N):
    offset = M
    for i in range(N):
        for j in range(N):
            if keyWithPadding[offset+i][offset+j] == lockWithPadding[offset+i][offset+j]:
                return False
    return True
   
def getRotateKey(key,M,rotateCnt):
    if rotateCnt == 0:
        return key
    newMat = []
    for i in range(M):
        newMat.append([])
        for j in range(M):
            newMat[i].append(0)
    for i in range(M):
        for j in range(M):
            if rotateCnt == 1:
                newMat[j][M-1-i] = key[i][j]
            elif rotateCnt == 2:
                newMat[M-1-i][M-1-j] = key[i][j]
            elif rotateCnt == 3:
                newMat[M-j-1][i] = key[i][j]
    return newMat

def solution(key, lock):
    M = len(key)
    N = len(lock)
    lockWithPadding = getLockWithPadding(lock,M,N)
    for rotateCnt in range(4):
        rotatedKey = getRotateKey(key,M,rotateCnt)
        for i in range(1,N+M):
            for j in range(1,N+M):
                keyWithPadding = getKeyWithPadding(rotatedKey,M,N,i,j)
                if check(keyWithPadding,lockWithPadding,M,N):
                    return True
    return False

def printNewMat(newMat):
    for i in range(len(newMat)):
        print(newMat[i])

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],[[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
#print(getLockWithPadding([[1, 1, 1], [1, 1, 0], [1, 0, 1]],3,3))
#print(getKeyWithPadding([[0, 0, 0], [1, 0, 0], [0, 1, 1]],3,3,1,0))

