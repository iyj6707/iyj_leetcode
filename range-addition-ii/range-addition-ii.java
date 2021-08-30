class Solution {
    public int maxCount(int m, int n, int[][] ops) {
        int minX = m;
        int minY = n;
        
        for (var op: ops) {
            minX = Math.min(op[0], minX);
            minY = Math.min(op[1], minY);
        }
        
        return minX * minY;
    }
}