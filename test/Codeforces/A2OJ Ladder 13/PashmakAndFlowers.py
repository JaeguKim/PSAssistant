#diff가 0이되는 케이스를 미처 생각하지 못하여 못한 문제
n = int(input())
b = [int(ch) for ch in input().split()]
dict = {}
minNum = pow(10,10)
maxNum = -1
for num in b:
    if num not in dict:
        dict[num] = 1
    else:
        dict[num] +=1
    minNum = min(minNum,num)
    maxNum = max(maxNum,num)
diff = maxNum-minNumㅌ
res = 0
if diff == 0:
    res = int(n*(n-1)/2)
else:
    for key in dict:
        if key+diff in dict:
            res+=dict[key+diff]*dict[key]
print('{} {}'.format(diff,res))

