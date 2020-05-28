from collections import deque

k = int(input())
lunlun = []
q = deque([1,2,3,4,5,6,7,8,9])
while len(lunlun) <= k:
    first = q.popleft()
    lunlun.append(first)
    if first%10-1 >= 0:
        q.append(first*10 + (first%10-1))
    q.append(first*10 + first%10)
    if first%10+1 <= 9:
        q.append(10*first + (first%10+1))
print(lunlun[k-1])