#30m
n = int(input())
heights = [int(ch) for ch in input().split(' ')]
s = sorted(heights)
min = s[0]
max = s[-1]
minIdx = -1
maxIdx = -1
for i in range(len(heights)-1,-1,-1):
    if heights[i] == min:
        minIdx = i
        break
for i in range(len(heights)):
    if heights[i] == max:
        maxIdx = i
        break
res = maxIdx+n-1-minIdx
if minIdx < maxIdx:
    res-=1
print(res)