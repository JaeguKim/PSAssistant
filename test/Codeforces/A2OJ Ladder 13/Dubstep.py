#5min
str=input()
ary=str.split('WUB')
for s in ary:
    if s != 'WUB' and len(s)>0:
        print(s,end=' ')