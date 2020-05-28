n,m = [int(ch) for ch in input().split()]
heights = [int(ch) for ch in input().split()]
graphs = []
for i in range(n):
    graphs.append([])
for i in range(m):
    roadInfo = [int(ch) for ch in input().split()]
    start = roadInfo[0]-1
    end = roadInfo[1]-1
    graphs[start].append(end)
    graphs[end].append(start)
res = []
for i in range(len(graphs)):
    isGood = True
    for v in graphs[i]:
        if heights[i] <= heights[v]:
            isGood = False
            break
    if isGood:
        res.append(i+1)
print(len(res))
