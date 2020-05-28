#dfs를 이용하여 쉽게 풀수있는문제, 구현이 문제가 아니라 아이디어를 연계하는것이 잘 안떠올랐다.
def dfs(graph,visit,vertex):
    if visit[vertex] == False:
        visit[vertex] = True
        for i in graph[vertex]:
            dfs(graph,visit,i)

n = int(input())
xAry = []
yAry = []
graph = []
for i in range(n):
    x,y = map(int,input().split())
    xAry.append(x)
    yAry.append(y)
    graph.append([])
for i in range(n):
    for j in range(n):
        if i != j:
            if xAry[i] == xAry[j] or yAry[i] == yAry[j]:
                graph[i].append(j)
res = -1
visit = [False]*n
for i in range(n):
    if visit[i] == False:
        dfs(graph,visit,i)
        res+=1
print(res)
