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

def SieveOfEratosthenes(n): 
      
    # Create a boolean array "prime[0..n]" and initialize 
    # all entries it as true. A value in prime[i] will 
    # finally be false if i is Not a prime, else true. 
    prime = [True for i in range(n + 1)] 
    p = 2
    while (p * p <= n): 
          
        # If prime[p] is not changed, then it is a prime 
        if (prime[p] == True): 
              
            # Update all multiples of p 
            for i in range(p * 2, n + 1, p): 
                prime[i] = False
        p += 1
    prime[0]= False
    prime[1]= False
    # Print all prime numbers 
    for p in range(n + 1): 
        if prime[p]: 
            print(p)

def myVersionOfSieveOfEratosthenes(n):
    prime = [True for i in range(n + 1)] 
    prime[0] = prime[1] = False
    p = 2
    while (p * p <= n): 
        if (prime[p] == True): 
            for i in range(p * 2, n + 1, p): 
                prime[i] = False
        p += 1
    return prime

def checkPerfectSquare(n):
    root = sqrt(n)
    if int(root+0.5)**2 == n:
        return True
    else: 
        return False

t = int(input())
nums = list(map(int,input().split()))
n = 10**12
primeCheck = myVersionOfSieveOfEratosthenes(int(sqrt(n)))
for num in nums:
    if checkPerfectSquare(num):
        root = int(sqrt(num))
        if primeCheck[root]==True:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')

