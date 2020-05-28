#44min -> 아이디어 생각하는데 생각보다 많이걸림
n = int(input()) * 2 + 1
map = []
for i in range(n):
    map.append([' ']*n)
for i in range(int(n/2)+1):
    num = 0
    for j in range(int(n/2)-i,int(n/2)+1):
        map[i][j] = str(num)
        map[i][n-1-j] = str(num)
        num+=1
    map[n-1-i] =  map[i].copy()

for line in map:
    str = ''.join(line).rstrip()
    for i in range(len(str)):
        if i == len(str)-1:
            print(str[i])
        else:
            print(str[i],end=' ')