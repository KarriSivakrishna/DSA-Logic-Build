class Solution:
    def maxLength(self, nums: List[int]) -> int:
        prod = 1
        res = 2
        left = 0

        for right, num in enumerate(nums):
            while gcd(prod, num) != 1:
                prod //= nums[left]
                left += 1
            prod *= num
            res = max(res, right - left + 1)

        return res