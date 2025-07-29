class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority=nums[0]
        cnt=0
        for i in range(len(nums)):
            if nums[i]==majority:
                cnt+=1
            else:
                cnt-=1
            if(cnt==0):
                majority=nums[i]
                cnt=1
        return majority