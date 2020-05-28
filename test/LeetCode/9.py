class Solution:
    def isPalindrome(self, x: int) -> bool:
        xStr = str(x)
        xStr = xStr[::-1]
        return (str(x)==xStr)

sol = Solution()
x = int(input())
print(sol.isPalindrome(x))