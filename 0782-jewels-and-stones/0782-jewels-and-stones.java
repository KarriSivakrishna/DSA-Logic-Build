class Solution {
    public int numJewelsInStones(String jewels, String stones) {
    HashMap<Character,Integer>H=new HashMap<>();
        for(int i=0;i<stones.length();i++){
            char ch=stones.charAt(i);
            H.put(ch,H.getOrDefault(ch,0)+1);

        }
        int ans=0;
        for(int i=0;i<jewels.length();i++){
            char ch=jewels.charAt(i);
            if(H.containsKey(ch)){
                ans+=H.get(ch);
            }
        }
        return ans;
    }
}