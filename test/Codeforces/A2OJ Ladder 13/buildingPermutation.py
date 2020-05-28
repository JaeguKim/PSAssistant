#문제를 정확히 이해하면 풀이가 간단해지는 경우
n = int(input())
p = list(map(int,input().split()))
p = sorted(p)
res = 0
for i in range(1,len(p)+1):
    res += abs(i-p[i-1])
print(res)



