class Solution:
    def threeConsecutiveOdds(self, arr):
        count = 0
        for num in arr:
            if num % 2 == 1:
                count += 1
                if count == 3:
                    return True
            else:
                count = 0
        return False