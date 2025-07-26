class Solution:
     def threeSum(self , nums):
         # Sort the input  array to use two-pointer  technique efficiently 
         nums.sort()
         
         # List to store  all unique triplets 
         result = []
         
         # Iterate over  the array with index  `i`
         for i in range (len(nums) - 2):
             # Skip duplicate  elements to avoid duplicate  triplets
             if i > 0  and nums[i] == nums [i - 1]:
                 continue 
            
             # Initialize  two pointers for the  current index `i`
             left, right  = i + 1, len(nums) -  1
            
             # Use while  loop to find pairs that  sum to -nums[i]
             while left  < right:
                 # Calculate  the sum of the trip let
                 total  = nums[i] + nums[left ] + nums[right]
                 
                 if total  == 0:
                     #  Append the found trip let to the result list 
                     result .append([nums[i], nums [left], nums[right]])
                     
                     #  Move both pointers and  skip duplicates
                     left  += 1
                     right  -= 1
                    
                     #  Skip duplicate elements  for 'left'
                     while  left < right and nums [left] == nums[left -  1]:
                          left += 1
                     #  Skip duplicate elements  for 'right'
                     while  left < right and nums [right] == nums[right  + 1]:
                          right -= 1
                
                 elif  total < 0:
                     #  If sum is less than  zero, move left pointer  to increase the sum 
                     left  += 1
                 else :
                     #  If sum is greater than  zero, move right pointer  to decrease the sum 
                     right  -= 1
        
         return result 