#20min
#dictionary로 hash를 만들때 초기화 값에 유의하자
s1 = [ch for ch in input()]
s2 = [ch for ch in input()]
s3 = [ch for ch in input()]
concat = s1+s2
dict = {}
for ch in s3:
    if ch not in dict.keys():
        dict[ch] = 1
    else:
        dict[ch] += 1
isPos = True
for ch in concat:
    if ch not in dict.keys():
        isPos = False
        break
    if dict[ch] <= 0:
        isPos = False
        break
    dict[ch] -= 1

for key in dict.keys():
    if dict[key] != 0:
        isPos = False
        break

if isPos:
    print('YES')
else:
    print('NO')