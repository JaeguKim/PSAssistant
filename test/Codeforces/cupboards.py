#7m
n = int(input())
left = {0:0, 1:0}
right = {0:0, 1:0}
for i in range(n):
    arr = input().split(' ')
    if int(arr[0]) == 0:
        left[0]+=1
    else:
        left[1]+=1
    if int(arr[1]) == 0:
        right[0]+=1
    else:
        right[1]+=1
res = min(left[0],left[1])+min(right[0],right[1])
print(res)
    