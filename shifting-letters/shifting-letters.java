class Solution {
//     public String shiftingLetters(String s, int[] shifts) {
//         StringBuilder sb = new StringBuilder();
//         int cnt = 0;
//         int charNum = 'z' - 'a' + 1;
        
//         for (int i = shifts.length - 1; i >= 0; i--) {
//             char ch = s.charAt(i);
//             cnt = (cnt + shifts[i]) % charNum;
            
//             sb.append((char) (ch + cnt > 'z' ? ch + cnt - charNum : ch + cnt));
//         }
        
//         return sb.reverse().toString();
//     }
    
    public String shiftingLetters(String s, int[] shifts) {
        StringBuilder sb = new StringBuilder();
        int charNum = 'z' - 'a' + 1;
        
        for (int i = shifts.length - 2; i >= 0; i--) {
            shifts[i + 1] %= charNum;
            shifts[i] += shifts[i + 1];
        }
        
        System.out.println(Arrays.toString(shifts));
        
        for (int i = 0; i < shifts.length; i++) {
            char ch = s.charAt(i);
            shifts[i] %= charNum;
            
            sb.append((char) (ch + shifts[i] > 'z' ? ch + shifts[i] - charNum : ch + shifts[i]));
        }
        
        return sb.toString();
    }
}