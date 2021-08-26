import java.util.*;

class Solution {
    public boolean judgeSquareSum(int c) {
        // a^2 + b^2 = (a + b)^2 - 2ab = c
        // c - b^2 = a^2
        int to = (int)Math.sqrt(c);
        double n = 0;
        for (int b = 0; b <= to; b++) {
            n = Math.sqrt(c - b * b);
            if (n == Math.ceil(n)) {
                return true;
            }
        }
        return false;
    }
}