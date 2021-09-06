class Solution {
    public char slowestKey(int[] releaseTimes, String keysPressed) {
        int duration = releaseTimes[0];
        char ansKey = keysPressed.charAt(0);
        
        for (int i = 1; i < releaseTimes.length; i++) {
            int time = releaseTimes[i] - releaseTimes[i - 1];
            char key = keysPressed.charAt(i);
            if (time > duration || (time == duration && key > ansKey)) {
                duration = time;
                ansKey = key; 
            }
        }
        
        return ansKey;
    }
}