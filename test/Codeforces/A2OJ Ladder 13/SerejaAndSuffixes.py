import sys
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
    
n,m = map(int,input().split())
a = list(map(int,input().split()))
check = [0]*(pow(10,5)+1)
res = {}
for i in range(n-1,-1,-1):
    if check[a[i]] == 0:
        check[a[i]] = 1
        if i+1 > n-1:
            res[i]=1
        else:
            res[i]=res[i+1]+1
    else:
        res[i] = res[i+1]
for i in range(m):
    num = int(input())
    print(res[num-1])


        
    
    

