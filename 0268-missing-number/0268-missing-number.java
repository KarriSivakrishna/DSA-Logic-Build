class Solution {
    public int missingNumber(int[] nums) {
        int n=nums.length;
        HashMap<Integer,Integer>H=new HashMap<>();
       for (int i=0;i<n;i++){
        H.put(nums[i],1);
       }
       for (int i=0;i<=n;i++){
        if(!H.containsKey(i)){
            return i;
        }
        
       }
     return -1;  
}
}