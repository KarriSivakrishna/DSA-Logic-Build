from typing import List
import heapq

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 3
        total = len(nums)

        # Step 1: Compute left prefix minimum sum of largest n elements
        left = [0] * total
        max_heap = []
        sum_left = 0

        for i in range(2 * n):
            heapq.heappush(max_heap, -nums[i])  # Use negative to simulate max-heap
            sum_left += nums[i]
            if len(max_heap) > n:
                sum_left += heapq.heappop(max_heap)  # Remove the largest
            if i >= n - 1:
                left[i] = sum_left

        # Step 2: Compute right suffix maximum sum of smallest n elements
        right = [0] * total
        min_heap = []
        sum_right = 0

        for i in range(total - 1, n - 1, -1):
            heapq.heappush(min_heap, nums[i])
            sum_right += nums[i]
            if len(min_heap) > n:
                sum_right -= heapq.heappop(min_heap)  # Remove the smallest
            if i <= 2 * n:
                right[i] = sum_right

        # Step 3: Find minimum difference between left and right
        min_diff = float('inf')
        for i in range(n - 1, 2 * n):
            diff = left[i] - right[i + 1]
            min_diff = min(min_diff, diff)

        return min_diff
