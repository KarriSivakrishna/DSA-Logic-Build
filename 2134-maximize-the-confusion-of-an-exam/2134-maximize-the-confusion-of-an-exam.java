class Solution {
    public int maxConsecutiveAnswers(String answerKey, int k) {
        int l = 0; 
        int ans = 0;  
        int n = answerKey.length(); 
        int cntT = 0;  
        int cntF = 0; 

        for (int r = 0; r < n; r++) {
            if (answerKey.charAt(r) == 'F') {
                cntF++;  
            } else {
                cntT++;  
            }

            
            while (Math.min(cntF, cntT) > k) {
                if (answerKey.charAt(l) == 'F') {
                    cntF--;  
                } else {
                    cntT--;  
                }
                l++;  // Move the left pointer
            }

           
            ans = Math.max(ans, r - l + 1);
        }
        
        return ans;  
    }
}
