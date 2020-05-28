#6m
num = input()

cnt = 0
for ch in num:
    if ch == '4' or ch == '7':
        cnt += 1
if cnt == 4 or cnt == 7:
    print("YES")
else:
    print("NO")