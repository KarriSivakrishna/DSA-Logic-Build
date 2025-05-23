class Solution {
    public int pivotIndex(int[] nums) {
     int postfix=0;
        for(int i:nums){
            postfix+=i;
        }
        int prefix=0;
        for(int i=0; i<nums.length; i++){
            postfix-=nums[i];
            if(prefix==postfix){
                return i;
            }
            prefix+=nums[i];
        }
        return -1;
    }
}