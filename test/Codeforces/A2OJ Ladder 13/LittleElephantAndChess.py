#10min
map = []
normal = ['WBWBWBWB','BWBWBWBW']
for i in range(8):
    str = input()
    if str not in normal:
        print('NO')
        exit()
print('YES')