class Solution {
    public String shiftingLetters(String s, int[] shifts) {
        StringBuilder sb = new StringBuilder();
        int cnt = 0;
        int charNum = 'z' - 'a' + 1;
        
        for (int i = shifts.length - 1; i >= 0; i--) {
            char ch = s.charAt(i);
            cnt = (cnt + shifts[i]) % charNum;
            
            sb.append((char) (ch + cnt > 'z' ? ch + cnt - charNum : ch + cnt));
        }
        
        return sb.reverse().toString();
    }
}