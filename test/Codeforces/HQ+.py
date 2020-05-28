#4min
line = input()
find = False
for ch in line:
    if ch == 'H' or ch == 'Q' or ch == '9':
        print('YES')
        find = True
        break
if find == False:
    print('NO')