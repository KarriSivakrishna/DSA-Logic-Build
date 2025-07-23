class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        x, y, z = sorted([a, b, c])
    
        # Calculate gaps
        gap1, gap2 = y - x - 1, z - y - 1
        
        # Minimum moves
        if gap1 == 0 and gap2 == 0:
            min_moves = 0
        elif gap1 <= 1 or gap2 <= 1:
            min_moves = 1
        else:
            min_moves = 2
        
        # Maximum moves
        max_moves = gap1 + gap2
        
        return [min_moves, max_moves]
        