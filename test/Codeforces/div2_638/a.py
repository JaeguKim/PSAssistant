t = int(input())
for i in range(t):
    n = int(input())
    list = []
    for j in range(n):
        list.append(pow(2,j+1))
    onepile = list[-1]+sum(list[0:int(n/2)-1])
    secpile = sum(list[int(n/2)-1:n-1])
    print(abs(secpile-onepile))

