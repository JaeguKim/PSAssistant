#1h 30m
#잘못된 가정을 찾는것이 런타임에러 해결의 핵심이다. 이 문제의 경우에 블럭의 번호가 1부터 순차적으로 부여된다고 내가 가정을 해서 50분만에 풀수있는 문제를 1시간 반동안 붙잡고 있었다.
#문제를 다시 정확히 읽는것이 중요하다
#dictionary는 루프도중 값을 제거하는것이 불가능하다

def canFill(board,block,n):
    sortByRow = sorted(block,key=lambda x: x[0])
    minRow = sortByRow[0][0]
    maxRow = sortByRow[-1][0]
    sortByCol = sorted(block,key=lambda x: x[1])
    minCol = sortByCol[0][1]
    maxCol = sortByCol[-1][1]
    
    emptyBlocks = []
    for row in range(minRow,maxRow+1):
        for col in range(minCol,maxCol+1):
            if [row,col] not in block:
                emptyBlocks.append([row,col])

    for block in emptyBlocks:
        for i in range(block[0]+1):
            if board[i][block[1]] != 0:
                return False
    return True


def makeBlockDict(board,n):
    blockDict = {}
    for i in range(n):
        for j in range(n):
            num = board[i][j]
            if num != 0:
                if num not in blockDict.keys():
                    blockDict[num] = []
                blockDict[num].append([i,j])

    return blockDict

def eraseBlock(board,block):
    for coord in block:
        row = coord[0]
        col = coord[1]
        board[row][col] = 0

def solution(board):
    n = len(board)
    blockDict = makeBlockDict(board,n)
    res = 0
    isErased = True
    while isErased:
        isErased = False
        keyListForRemove = []
        for key in blockDict.keys():
            block = blockDict[key]
            if canFill(board,block,n):
                eraseBlock(board,block)
                res+=1
                isErased = True
                keyListForRemove.append(key)
        for key in keyListForRemove:
            blockDict.pop(key)
    return res

print(solution([[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,4,0,0,0],[0,0,0,0,0,4,4,0,0,0],[0,0,0,0,3,0,4,0,0,0],[0,0,0,2,3,0,0,0,5,5],[1,2,2,2,3,3,0,0,0,5],[1,1,1,0,0,0,0,0,0,5]]))