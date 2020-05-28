#15min
import sys
import math
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
 
n,x = map(int,input().split())
nums = list(map(int,input().split()))
idxList = []
res = 0
if x not in nums:
    nums.append(x)
    res+=1
    n+=1
nums = sorted(nums)
middle = int(math.floor((n+1)/2))-1
for i in range(len(nums)):
    if nums[i]==x:
        idxList.append([i,abs(i-middle)])
idxList = sorted(idxList,key=lambda x:x[1])
curSize = n
curIdx = idxList[0][0]
while middle != curIdx:
    if middle < curIdx:
        curSize+=1
    elif middle > curIdx:
        curSize+=1
        curIdx+=1
    middle = int(math.floor((curSize+1)/2))-1
    res+=1
print(res)
