#37min - 구현력을 테스트 하는 문제
#경우를 신중하게 나눠야한다

def addDict(dict,num):
    if num not in dict:
        dict[num] = 1
    else:
        dict[num] += 1

n = int(input())
orders = list(map(int,input().split()))
dict = {}
for order in orders:
    if order == 25:
        addDict(dict,25)
    elif order == 50:
        if 25 not in dict or dict[25] == 0:
            print('NO')
            exit()
        else:
            dict[25] -= 1
            addDict(dict,50)
    elif order == 100:
        if 25 in dict and 50 in dict and dict[25]>0 and dict[50] >0:
            dict[25]-=1
            dict[50]-=1
        elif 25 in dict and dict[25] >= 3:
            dict[25]-=3
        else:
            print('NO')
            exit()
        addDict(dict,100)
print('YES')
