#16min
s,n = [int(ch) for ch in input().split()]
l2 = []
sum = s
for i in range(n):
    data = [int(ch) for ch in input().split()]
    if data[0] < s:
        sum += data[1]
    else:
        l2.append([data[0],data[1]])

isPos = True
l2 = sorted(l2,key=lambda x: x[0])
for elem in l2:
    if sum > elem[0]:
        sum+=elem[1]
    else:
        isPos = False
        break        
print('YES') if isPos else print('NO')


