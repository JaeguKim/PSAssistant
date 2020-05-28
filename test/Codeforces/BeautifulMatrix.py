#10min
row = 0
col = 0
for i in range(5):
    arr = input().split(' ')
    for j in range(len(arr)):
        if arr[j] == '1':
            row = i+1
            col = j+1
            res = abs(3-row) + abs(3-col)
            print(res)
            