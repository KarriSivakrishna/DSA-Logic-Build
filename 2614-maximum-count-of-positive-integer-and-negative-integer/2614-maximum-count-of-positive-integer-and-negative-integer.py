from typing import List

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n=len(nums)
        N_count = 0
        P_count = 0
        
        for i in range(n):
            if nums[i] < 0:
                N_count += 1
            elif nums[i] > 0:
                P_count += 1

        return max(N_count, P_count)
