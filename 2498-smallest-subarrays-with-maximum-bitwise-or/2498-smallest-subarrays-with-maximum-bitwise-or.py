class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ret = [0] * n
        i, j = n - 1, n - 1
        bitCount = [0] * 32
        
        # add bits of k to bitCount
        def addCount(k):
            cnt = 0
            while k > 0:
                bitCount[cnt] += k & 1
                k >>= 1
                cnt += 1
        
        # check if removing bits of k from bitCount decreases the current bitwise OR of numbers between i and j
        def checkCount(k):
            cnt = 0
            while k > 0:
                if k & 1 == 1 and bitCount[cnt] == 1:
                    return False
                k >>= 1
                cnt += 1
            return True
        
        # remove bits of k from bitCount
        def removeCount(k):
            cnt = 0
            while k > 0:
                bitCount[cnt] -= (k & 1)
                k >>= 1
                cnt += 1
        
        while i > -1:
            addCount(nums[i])
            while checkCount(nums[j]) and i < j:
                removeCount(nums[j])
                j -= 1
            i -= 1
            ret[i+1] = j - i
        
        return ret
            