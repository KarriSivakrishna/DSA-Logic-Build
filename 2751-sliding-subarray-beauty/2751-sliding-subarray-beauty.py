from sortedcontainers import SortedList
class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        beauts = []
        i = 0
        j = k
        LEN = len(nums)
        sortedL = SortedList(nums[i:j])
        while j - 1 < LEN:
            if x <= j and sortedL[x - 1] < 0:
                beauts.append(sortedL[x-1])
            else:
                beauts.append(0)
            if j < LEN:
                sortedL.add(nums[j])
            sortedL.discard(nums[i])
            i += 1
            j += 1
        return beauts