class Solution:
    def countTime(self, time: str) -> int:
        
        nonreplacable = []
        count  = 0

        for i in range(5):
            if time[i] != '?':
                nonreplacable.append(i)

        for i in range(24):
            for j in range(60):

                if i < 10:
                    hour = '0' + str(i)
                else:
                    hour = str(i)

                
                if j < 10:
                    minute = '0' + str(j)
                else:
                    minute = str(j)
                
                time_ = hour + ':' + minute 

                flag = 0
                for k in nonreplacable:
                    if time_[k] != time[k]:
                        flag = 1 
                        break
                if flag == 0:
                    count += 1
        return count