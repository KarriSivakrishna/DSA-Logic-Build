from itertools import combinations as comb
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dabba={}
        for j in range(len(nums)):
            if nums[j] not in dabba.keys():
                dabba[nums[j]]=[j]
            else:
                dabba[nums[j]].append(j)
        for j in dabba.values():
            for p,l in comb(j,2):
                if abs(p-l)<=k:
                    return True
        return False