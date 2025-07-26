class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        for i in range(n):
            for j in range(n):
                if(baskets[j] != "F" and fruits[i] <= baskets[j]):
                    baskets[j] = "F"
                    break

        unplace = 0
        for i in baskets:
            if i != "F":
                unplace += 1
        return unplace
