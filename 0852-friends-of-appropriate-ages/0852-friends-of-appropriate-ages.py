from collections import Counter
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        count=0
		# Step 1
        dicto=Counter(ages)
		# Step 2
        for me in dicto:
            my_age_count=dicto[me]
			# Step 3
            for age in dicto:
                if not (age<= 0.5 * me +7 or age>me):
					# Step 4 case (a)
                    if age!=me :
                        count+=dicto[age]*my_age_count
					# Step 4 case (b)
                    else:
                        count+=int(my_age_count*(my_age_count-1))
        return count