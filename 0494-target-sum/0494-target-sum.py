class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        cache = [dict() for i in range(len(nums)+1)]

        def dp(i,s):
            if i == len(nums):
                return int(s == target)
            if s not in cache[i]:
                cache[i][s] = dp(i+1,s+nums[i]) + dp(i+1,s-nums[i])
            return cache[i][s]
        
        return dp(0,0)
            