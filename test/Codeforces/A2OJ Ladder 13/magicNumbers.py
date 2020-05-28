#15min
#현재 알고리즘으로 처리할수 없는 경우가 있는지를 문제를 유심히 보면서 찾을수 있다.
num = input()
num = num.replace('144',' ')
num = num.replace('14',' ')
num = num.replace('1',' ')
num = num.replace(' ','')
if len(num) == 0:
    print('YES')
else:
    print('NO')