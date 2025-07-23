class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        l_occurance = 0
        r_occurance = 0
        choice = ''
        count = 0

        for i in moves:
            if i == 'L':
                l_occurance = l_occurance + 1
            elif i == 'R':
                r_occurance = r_occurance + 1

        if l_occurance > r_occurance:
            choice = 'L'
        elif l_occurance < r_occurance:
            choice = 'R'
        else:
            choice = 'L'

        moves = moves.replace('_', choice)

        for i in moves:
            if i == 'L':
                count = count - 1
            elif i == 'R':
                count = count + 1

        return abs(count)
                