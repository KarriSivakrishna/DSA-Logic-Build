class Solution:
    def minPairSum(self, nums: list[int]) -> int:
        nums.sort()
        pairs = []
        while nums:
            pairs.append(nums.pop(0) + nums.pop(-1))
        return max(pairs)
