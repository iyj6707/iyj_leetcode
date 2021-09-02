class Solution {
    
    public int arrayNesting(int[] nums) {
        int len = nums.length;
        int answer = 0;
        
        for (int i = 0; i < len; i++) {
            if (nums[i] == i) {
                answer = Math.max(answer, 1);
                continue;
            }
            
            int iterLen = 0;
            if (nums[i] != len) {
                int iter = nums[i];
                while (true) {
                    int tmp = iter;
                    iter = nums[iter];   
                    nums[tmp] = len;
                    if (iter == len) {
                        break;
                    }
                    iterLen++;
                }   
            }
            answer = Math.max(answer, iterLen);
            if (answer > Math.ceil(len / 2.0)) {
                return answer;
            }
        }
        return answer;
    }
}