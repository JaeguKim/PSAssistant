from collections import deque
n = int(input())
for i in range(n):
    s = [int(ch) for ch in input()]
    check={1:0,2:0,3:0}
    left=0;right=0
    que = deque()
    n = len(s)
    minLen = n
    isFind = False
    while True:
        if check[1]!=0 and check[2]!=0 and check[3]!=0:
            minLen = min(minLen,len(que))
            left+=1
            num = que.popleft()
            check[num]-=1
            isFind = True
        else:
            if right>len(s)-1:
                break
            que.append(s[right])
            check[s[right]]+=1
            right+=1
    if isFind == False:
        minLen = 0
    print(minLen)