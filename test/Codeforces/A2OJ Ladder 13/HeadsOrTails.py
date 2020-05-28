#11min
x,y,a,b = map(int,input().split())
list = []
for i in range(a,x+1):
    for j in range(b,y+1):
        if i>j:
            list.append([i,j])
print(len(list))
for pair in list:
    print('{} {}'.format(pair[0],pair[1]))
