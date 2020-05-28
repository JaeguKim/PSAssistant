class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        ans = 0
        sum = 0
        for i in range(-k,k):
            sum += cardPoints[i]
            if i>=0:
                sum -= cardPoints[i-k]
            ans = max(sum,ans)
        return ans 

print(Solution().maxScore(cardPoints = [1,2,3,4,5,6,1], k = 3))