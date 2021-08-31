class Solution {
    public int findMin(int[] nums) {
        int before = nums[0];
        for (var num: nums) {
            if (before > num) {
                return num;
            }
            before = num;
        }
        return nums[0];
    }
}