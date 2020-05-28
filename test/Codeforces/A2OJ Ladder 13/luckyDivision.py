#15min
def isLuckyNum(n):
    for ch in str(n):
        if ch != '4' and ch != '7':
            return False
    return True

n = int(input())
for i in range(1,n+1):
    if n % i == 0:
        if isLuckyNum(int(n/i)):
            print('YES')
            exit()
print('NO')