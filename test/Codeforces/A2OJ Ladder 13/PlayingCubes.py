#못품 - A번문제에서 풀이가 잘 생각안나는 경우, 변하지 않는 경우를 발견 하는것이 중요하다
n,m = map(int,input().split())
vasya = min(n,m)
petya = n+m-1-vasya
print('{} {}'.format(petya,vasya))

    



