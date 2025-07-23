class Solution:
    def generateTag(self, c: str) -> str:
        c=c.split()
        s='#' # taking first letter as #
        for i,j in enumerate(c):
            if i==0: # changing first letter after # to small
                s+=j.lower()
            else: # captilizes all words 
                s+=j.capitalize()
            # all words taken into s
        return s[:100] # only return 100 elements