#6m
line = input()
uNum = 0
lNum = 0
for ch in line:
    if ch.isupper():
        uNum += 1
    else:
        lNum += 1
res = ''
if uNum > lNum:
    print(line.upper())
else:
    print(line.lower())