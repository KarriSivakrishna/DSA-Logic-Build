class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:

        hs = defaultdict(int)
        sm = 0
        mx = 0
        i = 0
        j = 0

        while i < len(nums):
            hs[nums[i]] += 1
            if hs[nums[i]] >= 2:
                while hs[nums[i]] >= 2:
                    hs[nums[j]] -= 1
                    sm -= nums[j]
                    j += 1
                sm += nums[i]
            else:
                sm += nums[i]
                mx = max(mx, sm)
            i += 1
        
        return (mx)