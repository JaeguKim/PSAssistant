import sys
from math import sqrt
input = sys.stdin.readline

############ ---- Input Functions ---- ############
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))

def getDiffCh(oldChs,alphabets):
    for ch in alphabets:
        isSame = False
        for old in oldChs:
            if ch == old:
                isSame = True
        if isSame == False:
            return ch
            
n,k = invr()
stripes = insr()
alphabets = []
for i in range(k):
    alphabets.append(chr(ord('A')+i))
res = 0
i = 0
p = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'[: k] + 'A'
p = {p[i] : p[i + 1] for i in range(k)}
case1 = ['A','B']
case2 = ['B','A']
if k == 2:
    no_diff_caseA = 0; no_diff_caseB = 0
    for i in range(len(stripes)):
        if stripes[i] != case1[i%2]:
            no_diff_caseA+=1
        if stripes[i] != case2[i%2]:
            no_diff_caseB+=1
    ans = ''
    if no_diff_caseA < no_diff_caseB:
        print(no_diff_caseA)
        for i in range(len(stripes)):
            ans+=case1[i%2]
    else:
        print(no_diff_caseB)
        for i in range(len(stripes)):
            ans+=case2[i%2]
    print(ans)
    exit()

for i in range(1,n-1):
    if stripes[i] == stripes[i-1] and stripes[i] == stripes[i+1]:
        stripes[i] = p[stripes[i]]
        res+=1
for i in range(1,n):
    if stripes[i] == stripes[i-1]:
        stripes[i] = p[stripes[i]]
        res+=1

print(res)
print(''.join(stripes))

