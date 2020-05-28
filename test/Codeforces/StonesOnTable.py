n = int(input())
line = [ch for ch in input()]
idx = 0
cnt = 0
while idx < len(line) and idx+1 < len(line):
    if line[idx] == line[idx+1]:
        cnt+=1
    idx+=1

print(cnt)
