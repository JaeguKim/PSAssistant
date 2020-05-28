#42min -> 문제해석을 제대로 하자
n = int(input())
offset = int(n/2)
list = []
front = 1
last = n*n

for i in range(n):
    for j in range(offset):
        print(front,end=' ')
        front+=1
    for j in range(offset):
        print(last,end=' ')
        last-=1
    print()
