class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        res=""
        for i in word:
            if i.isalpha():
                res+=" "
            else:
                res+=i
        print(res)
        li=res.split(" ")
        print(li)
        ll=[]
        cnt=0
        for i in li:
            if i!='' and int(i) not in ll:
                ll.append(int(i))
                cnt+=1
        return cnt
        