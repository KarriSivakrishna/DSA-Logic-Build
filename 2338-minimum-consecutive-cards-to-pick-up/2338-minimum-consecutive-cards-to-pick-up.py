class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        
        min_len = float("inf")
        hash_table = {}

        for right, card in enumerate(cards):
            if card in hash_table:
                length = right - hash_table[card] + 1
                min_len = min(min_len, length)
            hash_table[card] = right

        return -1 if math.isinf(min_len) else min_len