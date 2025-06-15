class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        m = 0
        n = len(nums)
        for i in range(n):
            m = max(m, abs(nums[i] - nums[(i + 1) % n]))
        return m