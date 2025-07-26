class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        a1 = ord(coordinate1[0])-ord('a')+1
        a2 = int(coordinate1[1])
        
        b1 = ord(coordinate2[0])-ord('a')+1
        b2 = int(coordinate2[1])

        if (a1+a2) % 2 == (b1+b2) %2:
            return True

        return False


    