#codeforce에서 pypy 2.7이 가장 빠르므로 사용하도록 한다.
import sys
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
    
table = []
n,m,k = map(int,input().split())
rows = []
cols = []
for i in range(n):
    row = list(map(int,input().split()))
    table.append(row)
    rows.append(i)
for j in range(m):
    cols.append(j)
for i in range(k):
    query = input().split()
    q = query[0]
    n1 = int(query[1]); n2 = int(query[2])
    if q == 'c':
        temp = cols[n1-1]
        cols[n1-1] = cols[n2-1]
        cols[n2-1] = temp
    elif q == 'r':
        temp = rows[n1-1]
        rows[n1-1] = rows[n2-1]
        rows[n2-1] = temp
    elif q == 'g':
        row = rows[n1-1]
        col = cols[n2-1]
        print(table[row][col])

