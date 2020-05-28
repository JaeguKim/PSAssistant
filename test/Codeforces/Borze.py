#8m 52s
str = [i for i in input()]
res = []
i = 0
while i < len(str):
    if str[i] == '.':
        res += '0'
    elif i+1 <= len(str)-1:
        if str[i] == '-' and str[i+1] == '.':
            res += '1'
        else:
            res += '2'
        i+=1
    i+=1
print(''.join(res))

