class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        r1,r2,r3="qwertyuiopQWERTYUIOP","asdfghjklASDFGHJKL","zxcvbnmZXCVBNM"
        ans=[]
        
        for i in words:
            t=True
            r=""
            if i[0] in r1:
                r=r1
            elif i[0] in r2:
                r=r2
            elif i[0] in r3:
                r=r3
            for j in i:
                if j not in r:
                    t=False
                    break
            if t==True:
                ans.append(i)
        return ans