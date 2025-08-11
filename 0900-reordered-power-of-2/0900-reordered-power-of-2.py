class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        n_sorted = sorted(str(n))
        for i in range(31):  
            power = 1 << i
            if sorted(str(power)) == n_sorted:
                return True
        return False
