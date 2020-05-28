#2h 04min
from collections import deque
def solution(board):
    start = [[[0,0],[0,1]],0]
    moveOffset =[[-1,0],[1,0],[0,-1],[0,1]]
    rotate = [1,-1]
    visited = []
    n = len(board)
    que = deque()
    que.append(start)
    visited.append(start[0])
    while len(que) != 0:
        item = que.popleft()
        curPos = item[0]; curDist = item[1]
        if checkIfArrived(curPos,n):
            return curDist
        for offset in moveOffset:
            newPos = [[curPos[0][0]+offset[0],curPos[0][1]+offset[1]],
            [curPos[1][0]+offset[0],curPos[1][1]+offset[1]]]
            if checkPos(newPos,board,n,visited):
                visited.append(newPos)
                que.append([newPos,curDist+1])

        if curPos[0][0] == curPos[1][0]:
            for r in rotate:
                adjRow = [[curPos[0][0]+r,curPos[0][1]],[curPos[1][0]+r,curPos[1][1]]]
                if checkAdjacentRowORCol(adjRow,board,n) == False:
                    continue
                if board[adjRow[0][0]][adjRow[0][1]] == 0 and board[adjRow[1][0]][adjRow[1][1]] == 0:
                    newPos = [[curPos[0][0]+r,curPos[0][1]],curPos[0]]
                    if checkPos(newPos,board,n,visited):
                        visited.append(newPos)
                        que.append([newPos,curDist+1])
                    newPos = [[curPos[1][0]+r,curPos[1][1]],curPos[1]]
                    if checkPos(newPos,board,n,visited):
                        visited.append(newPos)
                        que.append([newPos,curDist+1])
        else:
            for r in rotate:
                adjCol = [[curPos[0][0],curPos[0][1]+r],[curPos[1][0],curPos[1][1]+r]]
                if checkAdjacentRowORCol(adjCol,board,n) == False:
                    continue
                if board[adjCol[0][0]][adjCol[0][1]] == 0 and board[adjCol[1][0]][adjCol[1][1]]==0:
                    newPos = [[curPos[0][0],curPos[0][1]+r],curPos[0]]
                    if checkPos(newPos,board,n,visited):
                        visited.append(newPos)
                        que.append([newPos,curDist+1])
                    newPos = [[curPos[1][0],curPos[1][1]+r],curPos[1]]
                    if checkPos(newPos,board,n,visited):
                        visited.append(newPos)
                        que.append([newPos,curDist+1])

def checkAdjacentRowORCol(pos,board,n):
    if checkBoundaray(pos,n) == False:
        return False
    if checkWall(pos,board) == False:
        return False
    return True

def checkPos(pos,board,n,visited):
    if checkBoundaray(pos,n) == False:
        return False
    if checkWall(pos,board) == False:
        return False
    for item in visited:
        if pos[0] in item and pos[1] in item:
            return False
    return True

def checkWall(curPos,board):
    for coord in curPos:
        row = coord[0]; col = coord[1]
        if board[row][col] == 1:
            return False
    return True

def checkBoundaray(curPos,n):
    for coord in curPos:
        row = coord[0]; col = coord[1]
        if not(row >= 0 and row < n and col >= 0 and col < n):
            return False
    return True

def checkIfArrived(curPos,n):
    for coord in curPos:
        if coord[0] == n-1 and coord[1] == n-1:
            return True
    return False

print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))
   
    
    
