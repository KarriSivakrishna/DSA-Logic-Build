
class Solution: 
    def checkValidCuts(self, n: int, rec: List[List[int]]) -> bool:
        # Sort rectangles by x-coordinates
        xl = sorted([(i[0], i[2]) for i in rec], key=lambda x: x[0])
        # Sort rectangles by y-coordinates
        yl = sorted([(i[1], i[3]) for i in rec], key=lambda x: x[0])
        
        # Function to check for valid cuts
        def has_valid_cut(intervals):
            c = 0
            ce = intervals[0][1]
            for start, end in intervals[1:]:
                if ce <= start:  # Found a gap
                    c += 1
                ce = max(ce, end)  # Update current end
                if c == 2:  # At least two disjoint parts
                    return True
            return False

        # Check for vertical and horizontal cuts
        return has_valid_cut(xl) or has_valid_cut(yl)