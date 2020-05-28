n,k = [int(num) for num in input().split(' ')]
map = []
for i in range(n):
    for j in range(n):
        if i == j:
            print(k,end=' ')
        else:
            print(0,end=' ')
    print()

        