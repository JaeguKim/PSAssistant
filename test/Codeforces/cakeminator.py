#19min
r,c = [int(num) for num in input().split(' ')]
map = []
for i in range(r):
    row =[ch for ch in input()]
    map.append(row)
ans = 0
for i in range(r):
    if 'S' not in map[i]:
        for j in range(c):
            if map[i][j] == '.':
                map[i][j] = '*'
                ans += 1

for i in range(c):
    cnt = 0
    isFind = False
    for j in range(r):
        if map[j][i] == 'S':
            isFind = True
            break
        if map[j][i] == '.':
            cnt+=1
    if isFind == False:
        ans += cnt
print(ans) 
        