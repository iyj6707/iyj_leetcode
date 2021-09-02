class Solution {
    public int numTrees(int n) {
        return dfs(n);
    }
    
    public static int dfs(int n) {
        int left;
        int right;
        int answer = 0;
        if (n == 0 || n == 1) {
            return 1;
        }
        for (int i = 1; i <= n; i++) {
            left = i - 1;
            right = n - i;
            answer += dfs(left) * dfs(right);
        }
        return answer;
    }
}