#TIME : 20min
import sys
from math import sqrt
input = sys.stdin.readline

def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))

class Solution:
    #def twoCitySchedCost(self, costs: List[List[int]]) -> int:
    def twoCitySchedCost(self,costs):
        cntA = len(costs)/2
        cntB = cntA
        res = 0
        sortedList = sorted(costs,key=lambda x:abs(x[0]-x[1]),reverse=True)
        for i in range(len(sortedList)):
            if sortedList[i][0] < sortedList[i][1]:
                if cntA > 0:
                    cntA -= 1
                    res += sortedList[i][0]
                else:
                    cntB -= 1
                    res += sortedList[i][1]
            else:
                if cntB > 0:
                    cntB -= 1
                    res += sortedList[i][1]
                else:
                    cntA -= 1    
                    res += sortedList[i][0]
        return res
sol = Solution()
testCase = [[10,20],[30,200],[400,50],[30,20]]
res = sol.twoCitySchedCost(testCase)
print(res)
