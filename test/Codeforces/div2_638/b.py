#생각하는 과정자체가 수열에 대한 감이 좀 필요하다는 생각이든다
def solve(n,k):
    s = set()
    for elem in input().split(' '):
        s.add(int(elem))
    if k < len(s):
        return print(-1)
    print(n*k)
    for i in range(n):
        for elem in s:
            print(elem,end=' ')
        for j in range(k-len(s)):
            print('1',end=' ')
    print()

t = int(input())
for i in range(t):
    n,k = [int(ch) for ch in input().split(' ')]
    solve(n,k)

    