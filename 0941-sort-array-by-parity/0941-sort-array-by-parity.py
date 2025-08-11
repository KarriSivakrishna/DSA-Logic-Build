class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0
        count = 0
        while count < n:
            if nums[i] % 2 == 1:
                nums = nums[:i] + nums[i+1:] + [nums[i]]
            else:
                i += 1
            count += 1
        return nums