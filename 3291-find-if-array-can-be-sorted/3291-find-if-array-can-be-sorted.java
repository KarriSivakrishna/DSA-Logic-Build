class Solution {
    // Helper function to count set bits in a number
    private int setBits(int num) {
        int count = 0;
        for (int i = 31; i >= 0; i--) {
            if ((num >> i & 1) == 1) {
                count++;
            }
        }
        return count;
    }

    // Helper function to check if the array is sorted
    private boolean check(int[] nums) {
        for (int i = 0; i < nums.length - 1; i++) {
            if (nums[i] > nums[i + 1]) {
                return false;
            }
        }
        return true;
    }

    public boolean canSortArray(int[] nums) {
        // Array to store the set bit count of each number
        int[] count = new int[nums.length];
        for (int j = 0; j < nums.length; j++) {
            count[j] = setBits(nums[j]);
        }

        int n = nums.length;
        int k = 0;
        while (k < n) {
            for (int i = 1; i < n; i++) {
                if (count[i] == count[i - 1] && nums[i] < nums[i - 1]) {
                    // Swap elements in nums array
                    int temp = nums[i];
                    nums[i] = nums[i - 1];
                    nums[i - 1] = temp;
                }
            }
            // Check if the array is sorted
            if (check(nums)) {
                return true;
            }
            k++;
        }
        return false;
    }
}