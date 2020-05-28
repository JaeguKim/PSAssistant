#26min - 중구남방으로 생각하지말고 차근차근 확실히 머리속에 그려질때 코딩하자
n,m = map(int,input().split())
data = []
rowData = []
for i in range(m):
    data.append([])
for i in range(n):
    str = input()
    line = [int(ch) for ch in str]
    rowData.append(line)
    for j in range(m):
        data[j].append(line[j])
maxList = []
for i in range(m):
    maxList.append(max(data[i]))
res = 0
for i in range(n):
    for j in range(len(rowData[i])):
        if rowData[i][j] == maxList[j]:
            res+=1
            break
print(res)
        

