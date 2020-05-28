#7min 26s
str1 = input().lower()
str2 = input().lower()
list = [str1,str2]
list.sort()
if str1 == str2:
    print('0')
else:
    if list[0] == str1:
        print('-1')
    else:
        print('1')
