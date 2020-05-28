#10m
n = int(input())
arr = [int(ch) for ch in input().split(' ')]
min = -1
max = -1
cnt = 0
for i in range(len(arr)):
    if i == 0:
        min = arr[i]
        max = arr[i]
        continue
    if min > arr[i]:
        cnt+=1
        min = arr[i]
    if max < arr[i]:
        cnt+=1
        max = arr[i]
print(cnt)