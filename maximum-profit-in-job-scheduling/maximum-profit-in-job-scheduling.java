class Job {
    int startTime;
    int endTime;
    int profit;
    
    Job(int startTime, int endTime, int profit) {
        this.startTime = startTime;
        this.endTime = endTime;
        this.profit = profit;
    }
}

class Solution {
    public int jobScheduling(int[] startTime, int[] endTime, int[] profit) {
        int len = startTime.length;
        Job[] jobs = new Job[len];
        
        // initiallize
        for (int i = 0; i < len; i++) {
            jobs[i] = new Job(startTime[i], endTime[i], profit[i]);
        }
        
        Arrays.sort(jobs, (a, b) -> a.endTime - b.endTime);
            
        int[] dp = new int[len];
        dp[0] = jobs[0].profit;
        for (int i = 1; i < len; i++) {
            int idx = binarySearch(jobs, i);
            if (idx != -1) {
                dp[i] = Math.max(dp[i - 1], dp[idx] + jobs[i].profit);   
            } else {
                dp[i] = Math.max(dp[i - 1], jobs[i].profit);
            }
        }
        
        return dp[len - 1];
    }
    
    public static int binarySearch(Job[] jobs, int idx) {
        int low = 0;
        int high = idx - 1;
        
        while (low <= high) {        
            int mid = (low + high) / 2;
            if (jobs[mid].endTime <= jobs[idx].startTime) {
                if (jobs[mid + 1].endTime <= jobs[idx].startTime) {
                    low = mid + 1;
                } else {
                    return mid;
                }
            } else {
                high = mid - 1;
            }
        }
        
        return -1;
    }
}