class Solution {
    public int findMin(int[] nums) {
        int left = 0;
        int right = nums.length - 1;
        if (nums.length == 1) {
            return nums[0];
        }
        
        if (nums[left] < nums[right]) {
            return nums[left];
        }

        while(true) {
            int mid = (left + right) / 2;
            if (nums[left] < nums[mid]) {
                left = mid;
            } else if (nums[left] > nums[mid]) {
                right = mid;
            } else {
                break;
            }
        }
        return nums[left + 1];
    }
}