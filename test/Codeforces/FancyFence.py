#38m 
#생각하는 속도보다 타이핑하려는 속도가 빠르다는 것은 조급하다는 것
#좀더 생각을 신속하되 정확하게 하려고 개선하자
def solve(a):
    n = 360/(180-a)
    if n.is_integer():
        return True
    else:
        return False
        
n = int(input())
for i in range(n):
    t = int(input())
    if solve(t):
        print('YES')
    else:
        print('NO')