#11min
str = input()
res = 0
prev = ''
for i in range(len(str)):
    if prev == str[i]:
        res+=1
        if res >= 7:
            print('YES')
            exit()
    else:
        prev=str[i]
        res=1
print('NO')
