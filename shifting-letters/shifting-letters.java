class Solution {
    public String shiftingLetters(String s, int[] shifts) {
        int charNum = 'z' - 'a' + 1;
        
        char[] arr = s.toCharArray();
        int len = shifts.length;
        int cnt = 0;
        
        for (int i = len - 1; i >= 0; i--) {
            char ch = arr[i];
            cnt = (cnt + shifts[i]) % charNum;
            
            arr[i] = (char) (ch + cnt > 'z' ? ch + cnt - charNum : ch + cnt);
        }
        
        return new String(arr);
    }
    
//     public String shiftingLetters(String s, int[] shifts) {
//         StringBuilder sb = new StringBuilder();
//         long cnt = 0;
//         int charNum = 'z' - 'a' + 1;
        
//         for (int i = shifts.length - 1; i >= 0; i--) {
//             char ch = s.charAt(i);
//             // cnt = (cnt + shifts[i]) % charNum;
//             cnt += shifts[i];
            
//             sb.append((char) ((ch - 'a' + cnt) % charNum + 'a'));
//         }
        
//         return sb.reverse().toString();
//     }
    
//     public String shiftingLetters(String s, int[] shifts) {
//         StringBuilder sb = new StringBuilder();
//         int charNum = 'z' - 'a' + 1;
        
//         for (int i = shifts.length - 2; i >= 0; i--) {
//             shifts[i + 1] %= charNum;
//             shifts[i] += shifts[i + 1];
//         }
        
//         for (int i = 0; i < shifts.length; i++) {
//             char ch = s.charAt(i);
//             shifts[i] %= charNum;
            
//             sb.append((char) (ch + shifts[i] > 'z' ? ch + shifts[i] - charNum : ch + shifts[i]));
//         }
        
//         return sb.toString();
//     }
}