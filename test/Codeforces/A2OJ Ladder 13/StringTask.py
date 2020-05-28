#15min
str = [ch for ch in input().lower()]
idx = 0
cons = ["a","o","y","e","u","i"]
while idx < len(str):
    if str[idx] in cons:
        str.remove(str[idx])
    else:
        str.insert(idx,'.')
        idx+=2
    
res = ''.join(str)
print(res)   

