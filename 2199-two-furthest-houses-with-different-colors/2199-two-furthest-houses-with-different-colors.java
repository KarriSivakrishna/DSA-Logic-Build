class Solution {
    public int maxDistance(int[] colors) {
        int n = colors.length;
        int max = 0;
        for (int i = 0; i < n; i++) {
            if (colors[i] != colors[n - 1]) {
                max = Math.max(max, n - 1 - i);
                break;
            }
        }

        for (int k = n - 1; k >= 1; k--) {
            if (colors[0] != colors[k]) {
                max = Math.max(max, k);
                break;
            }
        }

        return max;
    }
}
