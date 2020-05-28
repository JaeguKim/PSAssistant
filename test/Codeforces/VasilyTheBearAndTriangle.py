#25m
x,y = [int(num) for num in input().split(' ')]
yCoord = (abs(x)+abs(y)) * int(y/abs(y))
coord1 = (0,yCoord)
xCoord = (abs(x)+abs(y)) * int(x/abs(x))
coord2 = (xCoord,0)
if coord1[0] < coord2[0]:
    print(coord1[0],end=' ')
    print(coord1[1],end=' ')
    print(coord2[0],end=' ')
    print(coord2[1])
else:
    print(coord2[0],end=' ')
    print(coord2[1],end=' ')
    print(coord1[0],end=' ')
    print(coord1[1])
   