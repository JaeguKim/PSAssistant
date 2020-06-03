#TIME : 
import sys
from math import sqrt

testCase = [False,True]
def isBadVersion(n):
    return testCase[n-1]

class Solution:
    def firstBadVersion(self, n):
        if n==1:
            return 1
        l=1; r=n
        while True:
            mid = int((l+r)/2)
            v_mid = isBadVersion(mid)
            v_midPlusOne = isBadVersion(mid+1)
            if v_mid == False and v_midPlusOne == True:
                return mid+1
            elif v_mid == False and v_midPlusOne == False:
                l = mid+1
            elif v_mid == True and v_midPlusOne == True:
                if mid == 1:
                    return mid
                else:
                    r = mid-1
        """
        :type n: int
        :rtype: int
        """

sol = Solution()
res = sol.firstBadVersion(2)
print(res)