class Solution {
    public int totalFruit(int[] fruits) {
        HashMap<Integer,Integer>H=new HashMap<>();
        int l=0;
        int n=fruits.length;
        int ans=0;
        for(int r=0;r<n;r++){
            int val=fruits[r];
            H.put(val,H.getOrDefault(val,0)+1);
           while (H.size() > 2) {
                int lval = fruits[l];
                if (H.containsKey(lval)) {  
                    H.put(lval, H.get(lval) - 1); 
                    if (H.get(lval) == 0) {
                        H.remove(lval);  
                    }
                }
                l++;
                 
            }
            ans=Math.max(ans,r-l+1);
        }
        return ans;
    }
}