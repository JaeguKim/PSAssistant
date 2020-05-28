#23min 
#생각보다 간단한문제
n = int(input())
segments = []
minL = pow(10,10)
maxR = -1
for i in range(n):
    l,r = map(int,input().split())
    segments.append([l,r])
    minL = min(l,minL)
    maxR = max(r,maxR)
for i in range(len(segments)):
    if segments[i][0] == minL and segments[i][1] == maxR:
        print(i+1)
        exit()
print(-1)



