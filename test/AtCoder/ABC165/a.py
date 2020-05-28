k = int(input())
a,b = [int(ch) for ch in input().split()]
if a%k == 0:
    print('OK')
else:
    if int(a/k)*k + k <= b:
        print('OK')
    else:
        print('NG')
