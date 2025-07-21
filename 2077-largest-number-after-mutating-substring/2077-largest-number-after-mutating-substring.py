class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        n = len(num)
        res = ""
        flag = False
        end = -1
        for i in range(n):
            val = int(num[i])
            change_val = change[val]


            if(change_val > val):
                print(change_val)
                res += str(change_val)
                flag = True
            else:
                if(flag and change_val != val):
                    end = i
                    break
                res+= num[i]
        if(end != -1): res+= num[end:]
                


        return res