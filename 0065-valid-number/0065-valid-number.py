class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        numSeen = dotSeen = eSeen = False
        numAfterE = True

        for i, c in enumerate(s):
            if c.isdigit():
                numSeen = True
                if eSeen:
                    numAfterE = True
            elif c in ['+', '-']:
                if i != 0 and s[i-1].lower() != 'e':
                    return False
            elif c == '.':
                if dotSeen or eSeen:
                    return False
                dotSeen = True
            elif c.lower() == 'e':
                if eSeen or not numSeen:
                    return False
                eSeen = True
                numAfterE = False
            else:
                return False
        return numSeen and numAfterE
