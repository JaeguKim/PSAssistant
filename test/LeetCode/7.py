x = int(input())
s = str(x).rstrip('0')
reversedStr = ''
if x >= 0:
    if x == 0:
        print(0)
        exit()
    reversedStr = s[::-1]
else:
    reversedStr = s[-1:0:-1]
    reversedStr = '-'+reversedStr
x = int(reversedStr)
if x < pow(2,31) * (-1) or x > pow(2,31)-1:
    print(0)
    exit()
print(reversedStr)
