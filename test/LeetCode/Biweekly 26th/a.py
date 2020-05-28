class Solution:
    def maxPower(self, s: str) -> int:
        n = len(s)
        if n == 1:
            return 1
        if n == 2:
            return 2 if s[1] == s[0] else 1
        maxi = -1
        cnt = 1
        for i in range(1,n):
            if s[i] == s[i-1]:
                cnt+=1
            else:
                maxi = max(cnt,maxi)
                cnt=1
        return max(maxi,cnt)

sol = Solution()
print(sol.maxPower("leetcode"))
print(sol.maxPower("abbcccddddeeeeedcba"))
print(sol.maxPower("cc"))
print(sol.maxPower("aabbbbbccccdddddddeffffffggghhhhhiiiiijjjkkkkkllllmmmmmnnnnnoopppqrrrrsssttttuuuuvvvvwwwwwwwxxxxxyyyzzzzzzzz"))

