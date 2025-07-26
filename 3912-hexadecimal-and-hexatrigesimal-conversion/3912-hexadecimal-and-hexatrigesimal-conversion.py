class Solution:
    def concatHex36(self, n: int) -> str:
        def convert(num,b):
            if(num==0):
                return "0"
            if(b==16):
                digits="0123456789ABCDEF"
            else:
                digits="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            res=""
            while(num):
                rem=num%b
                res=digits[rem]+res
                num//=b
            return res
        return convert(n*n,16)+convert(n*n*n,36)
            