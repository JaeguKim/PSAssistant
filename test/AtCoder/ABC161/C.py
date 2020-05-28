str = input().split()
n = int(str[0])
k = int(str[1])
t = n%k
other = abs(k-t)
print(min(t,other))