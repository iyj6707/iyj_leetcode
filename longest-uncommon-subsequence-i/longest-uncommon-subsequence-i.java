class Solution {
    public int findLUSlength(String a, String b) {
        return(a.length() == b.length() && a.equals(b) ? -1 : Math.max(a.length(), b.length()));
    }
}