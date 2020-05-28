#26min
n,x = map(int,input().split())
cardList = [int(ch) for ch in input().split()]
s = abs(sum(cardList))
ans = int(s/x)
if s%x != 0:
    ans+=1
print(ans)
