#24min
n = int(input())
list = [1,2,3,4,5,6,7,8,9,10,10,10,10,11]
cnt = 0
for i in range(len(list)):
    if list[i] == n-10:
        cnt+=1
res = cnt * 4
if n-10 == 10:
    res -= 1
print(res)