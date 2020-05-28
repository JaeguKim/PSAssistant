import sys
from math import sqrt
input = sys.stdin.readline

############ ---- Input Functions ---- ############
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))

grid = []
visited = []
cntOfCell = 0
def dfs(r,c,res,listSize):
    if len(res) == listSize:
            return
    if visited[r][c] == False:
        #print('{} {}'.format(r,c))
        visited[r][c] = True
        res.append((r,c))
        if grid[r+1][c] == '.' and visited[r+1][c] == False:
            dfs(r+1,c,res,listSize)
        if grid[r-1][c] == '.' and visited[r-1][c] == False:
            dfs(r-1,c,res,listSize)
        if grid[r][c+1] == '.' and visited[r][c+1] == False:
            dfs(r,c+1,res,listSize)
        if grid[r][c-1] == '.' and visited[r][c-1] == False:
            dfs(r,c-1,res,listSize)
    
n,m,k = invr()
visited.append([True]*(m+2))
grid.append(['#']*(m+2))
for i in range(n):
    row = ['#']
    # for ch in insr():
    #     if ch == '.':
    #         cntOfCell+=1
    #     row.append(ch)
    for i in range(500):
        row.append('#')
    row.append('#')
    grid.append(row)
    visitRow = [True]
    for i in range(m):
        visitRow.append(False)
    visitRow.append(True)
    visited.append(visitRow)
grid.append(['#']*(m+2))
visited.append([True]*(m+2))

res = []
def printResult():
    if len(res) > 0:
        for i in range(1,n+1):
            for j in range(1,m+1):
                if grid[i][j] == '.':
                    if (i,j) not in res:
                        grid[i][j] = 'X'
    for i in range(1,n+1):
        print(''.join(grid[i][1:m+1]))

if k>0 and cntOfCell > 0:
    for i in range(1,n+1):
        for j in range(1,m+1):
            if grid[i][j] == '.' and visited[i][j] == False:
                dfs(i,j,res,cntOfCell-k)
                if len(res) == cntOfCell-k:
                    printResult()
else:
    printResult()


