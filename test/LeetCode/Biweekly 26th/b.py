class Solution:
    def simplifiedFractions(self, n: int):
        res = []
        strList = []
        for i in range(2,n+1):
            for j in range(1,i):
                num = j/i
                if num not in res:
                    res.append(num)
                    strList.append("{}/{}".format(j,i))
        return strList

sol = Solution()
print(sol.simplifiedFractions(2))
print(sol.simplifiedFractions(3))
print(sol.simplifiedFractions(4))
print(sol.simplifiedFractions(1))

