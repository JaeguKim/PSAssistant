#9m52s
n,k,l,c,d,p,nl,np = map(int,input().split())
drinkNum = int(k*l /(nl))
limeNum = c*d
saltNum = int(p/np)
res = int(min(saltNum,min(drinkNum,limeNum)) / n)
print(res)

