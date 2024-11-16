class Solution {
    public int[] resultsArray(int[] nums, int k) {
        int cnt = 1, len=nums.length;
        int[] res = new int[len-k+1];
        Arrays.fill(res, -1);

        for(int i=0; i<len; i++){
            if(i>0 && nums[i] == nums[i-1]+1) cnt++;
            else cnt = 1;

            if(cnt >= k) res[i+1-k] = nums[i];
        }

        return res;
    }
}