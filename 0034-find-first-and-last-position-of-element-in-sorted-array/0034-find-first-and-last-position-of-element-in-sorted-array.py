class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 1 and nums[0] == target:
            return [0, 0]

        left, right = 0, len(nums) - 1
        res = []
        while left <= right:
            if nums[left] == target:
                res.append(left)
                while left <= right:
                    if nums[right] == target:
                        res.append(right)
                        break
                    right -= 1
                return res
            left += 1
        return [-1, -1]