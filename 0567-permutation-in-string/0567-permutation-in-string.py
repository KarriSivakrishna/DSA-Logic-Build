class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): 
            return False
        
        s1count = defaultdict(int)
        for char in s1: 
            s1count[char] += 1 
        
        window = defaultdict(int)
        for char in s2[:len(s1)]:
            window[char] += 1
        
        if window == s1count:
            return True

        for i in range(len(s1), len(s2)): 
            newchar = s2[i]
            oldchar = s2[i - len(s1)] 

            window[oldchar] -= 1
            window[newchar] += 1
            if window[oldchar] == 0: 
                del window[oldchar] 
        
            if window == s1count: 
                return True 
        
        return False