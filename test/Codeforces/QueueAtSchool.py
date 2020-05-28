#21m 42s
n,t = [int(elem) for elem in input().split(' ')]
queue = [ ch for ch in input()]
cont = 0
isSwap = False
for rep in range(t):
    for i in range(n):
        if isSwap == True:
            isSwap = False
            continue
        if queue[i] == 'B' and i+1 <= n-1 and queue[i+1] == 'G':
            queue[i] = 'G'
            queue[i+1] = 'B'
            isSwap = True
print(''.join(queue))    

 
      