#6min
dict = {}
line = input()
for ch in line:
    dict[ch] = 1
if len(dict) %2 == 0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')