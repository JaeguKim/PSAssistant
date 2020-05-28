s = [ch for ch in input()]
ans = -1
for i in range(len(s)-1):
    zeroCnt = 0
    oneCnt = 0
    leftStr = s[0:i+1]
    rightStr = s[i+1:]
    for ch in leftStr:
        if ch == '0':
            zeroCnt += 1
    for ch in rightStr:
        if ch == '1':
            oneCnt += 1
    ans = max(zeroCnt+oneCnt,ans)
print(ans)

