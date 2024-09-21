class Solution {
    public int numOfSubarrays(int[] arr, int k, int threshold) {
        int ans=0;
        int n=arr.length;
        int l=0;
        int temp=0;
        for(int r=0;r<n;r++){
            temp=temp+arr[r];
            if(r-l==k){
                temp=temp-arr[l];
                l++;
            }
            if(r-l+1==k){
               if(temp/k >=threshold){
                ans++;
               }
            }
           
        }
        return ans;
    }
}