#13min
str = input()
hash = {}
for ch in str:
    if ch not in hash:
        hash[ch] = 1
    else:
        hash[ch]+=1
x = 0
for key in hash:
    if hash[key] %2 == 1:
        x+=1
if x == 0:
    print('First')
else:
    if x%2 == 0:
        print('Second')
    else:
        print('First')
