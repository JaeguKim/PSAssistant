class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0; right = 0
        list = []
        maximum = -1
        if len(s) == 0:
            return 0
        while right < len(s):
            if s[right] not in list:
                list.append(s[right])
                right+=1
                maximum = max(len(list),maximum)
            else:
                list.remove(s[left])
                left+=1
        return maximum
sol = Solution()
sol.lengthOfLongestSubstring("abcabcbb")
            