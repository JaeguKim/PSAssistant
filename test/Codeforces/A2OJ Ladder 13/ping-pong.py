import sys
from math import sqrt
from collections import deque
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

def canMove(a,b,c,d):
    if (a > c and a < d) or (b > c and b < d):
        return True
    return False

def bfs(graph,start,end):
    myQueue = deque()
    myQueue.append(start-1)
    visited = [False]*len(graph)
    while len(myQueue) != 0:
        cur = myQueue.popleft()
        visited[cur] = True
        for adjNode in graph[cur]:
            if adjNode+1 == end:
                return True
            if visited[adjNode] == False:
                myQueue.append(adjNode)
    return False

n = int(input())
intervals = []
graph = []
for i in range(n):
    line = inlt()
    start = line[1]; end = line[2]
    if line[0] == 1:
        intervals.append([start,end])
        graph.append([])
        n = len(graph)
        for i in range(n-1):
            if canMove(start,end,intervals[i][0],intervals[i][1]):
                graph[-1].append(i)
            if canMove(intervals[i][0],intervals[i][1],start,end):
                graph[i].append(n-1)
    elif line[0] == 2:
        if bfs(graph,start,end):
            print('YES')
        else:
            print('NO')
    