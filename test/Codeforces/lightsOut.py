#27min 03s
res = [[1,1,1],[1,1,1],[1,1,1]]

for i in range(3):
    arr = input().split(' ')
    for j in range(3):
        val = int(arr[j]) % 2
        if val == 1:
            res[i][j] = 0 if res[i][j] == 1 else 1
            if i+1 < 3:
                res[i+1][j] = 0 if res[i+1][j] == 1 else 1
            if i-1 > -1:
                res[i-1][j] = 0 if res[i-1][j] == 1 else 1
            if j+1 < 3:
                res[i][j+1] = 0 if res[i][j+1] == 1 else 1
            if j-1 > -1:
                res[i][j-1] = 0 if res[i][j-1] == 1 else 1
for i in range(3):
    temp = ''
    for j in range(3):
        temp += str(res[i][j])
    print(temp)