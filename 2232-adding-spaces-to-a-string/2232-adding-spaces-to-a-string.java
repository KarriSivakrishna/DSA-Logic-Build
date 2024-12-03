class Solution {
    public String addSpaces(String s, int[] spaces) {
        int len = s.length() + spaces.length;  
        StringBuilder res = new StringBuilder(len);
        int it = 0;                                

        for (int i = 0; i < s.length(); i++) {
            if (it < spaces.length && i == spaces[it]) {
                res.append(' ');
                it++;
            }
            res.append(s.charAt(i));              
        }

        return res.toString();
    }
}