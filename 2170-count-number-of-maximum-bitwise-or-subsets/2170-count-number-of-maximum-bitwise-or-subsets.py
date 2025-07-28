class Solution:
    def countMaxOrSubsets(self, nums: list[int]) -> int:
        #max possible OR
        target = 0
        for x in nums:
            target |= x

        n = len(nums)
        count = 0
        for mask in range(1, 1 << n):
            curr = 0
            # Build OR for this subset
            for i in range(n):
                if (mask >> i) & 1:
                    curr |= nums[i]
                    if curr == target:
                        break
            if curr == target:
                count += 1

        return count