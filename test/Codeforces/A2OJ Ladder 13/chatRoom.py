#15min
line = input()
str = 'hello'
idx = 0
for i in range(len(line)):
    if line[i] == str[idx]:
        idx+=1
        if idx > len(str)-1:
            break
if idx == len(str):
    print('YES')
else:
    print('NO')