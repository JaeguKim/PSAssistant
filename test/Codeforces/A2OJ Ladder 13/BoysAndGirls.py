#20min
f1 = open('input.txt','r')
f2 = open('output.txt','w+')
n,m = map(int,f1.readline().split())
ch = ''
pair = ''
if n>m:
    ch = 'B'
    pair = 'BG'
elif n<m:
    ch = 'G'
    pair = 'GB'
else:
    pair = 'GB'
for i in range(min(n,m)):
    f2.write(pair)
for i in range(abs(n-m)):
    f2.write(ch)
f1.close()
f2.close()