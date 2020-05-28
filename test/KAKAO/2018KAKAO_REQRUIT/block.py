#understanding : 2min
#coding : 
#total : 

def solution(m, n, board):
    map = []
    for i in range(m):
        list = []
        for j in range(n):
            list.append(board[i][j])
        map.append(list)

    while True:
        squareSet = set()
        for i in range(m-1):
            for j in range(n-1):
                ij = map[i][j]
                if ij == ' ':
                    continue
                if ij == map[i][j+1] and ij == map[i+1][j] and ij == map[i+1][j+1]:
                    squareSet.add((i,j))
                    squareSet.add((i,j+1))
                    squareSet.add((i+1,j))
                    squareSet.add((i+1,j+1))
        if len(squareSet) == 0:
            cnt = 0
            for i in range(m):
                for j in range(n):
                    if map[i-1][j-1] == ' ':
                        cnt+=1
            return cnt
        for elem in squareSet:
            row = int(elem[0])
            col = int(elem[1])
            map[row][col] = ''
        for col in range(n):
            colStr = ''
            for row in range(m):
                colStr += map[row][col]
            for i in range(m-len(colStr)):
                colStr = " " +colStr
            for i in range(len(colStr)):
                map[i][col] = colStr[i]

print(solution(2,2,["AA", "AA"]))
print(solution(2,2, ["AA", "AB"]))
print(solution(3,2, ["AA", "AA", "AB"]))
print(solution(4,2, ["CC", "AA", "AA", "CC"]))
print(solution(6,2, ["DD", "CC", "AA", "AA", "CC", "DD"]))
print(solution(8,2, ["FF", "AA", "CC", "AA", "AA", "CC", "DD", "FF"]))
#print(solution(8,2, ["AA", "AA", "CC", "AA", "AA", "DD"]))