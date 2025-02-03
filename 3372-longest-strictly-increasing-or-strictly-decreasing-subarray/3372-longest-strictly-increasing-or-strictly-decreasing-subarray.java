class Solution {
    public int longestMonotonicSubarray(int[] nums) {
    int incre = 1;
    int decre = 1;
    int maxLen = 1;
    int n = nums.length;

    for (int i = 1; i < n; i++) {
        if (nums[i] > nums[i - 1]) { 
            incre++;
            decre = 1;
        } 
        else if (nums[i] < nums[i - 1]) { 
            decre++;
            incre = 1;
        } 
        else { 
            incre = 1;
            decre = 1;
        }

        maxLen = Math.max(maxLen, Math.max(incre, decre));
    }
    return maxLen;
}

}