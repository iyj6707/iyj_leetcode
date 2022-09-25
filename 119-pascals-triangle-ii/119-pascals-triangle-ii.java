class Solution {
    public List<Integer> getRow(int rowIndex) {
        List<Integer> pre = new ArrayList<>();
        
        if(rowIndex == 0){
            return List.of(1);
        }
        
        pre.add(1);
        
        for(int i=1; i<=rowIndex; i++){
            List<Integer> curr = new ArrayList<>();
            
            curr.add(1);
            for(int j=1; j<i; j++){
                curr.add(pre.get(j-1)+pre.get(j));
            }
            curr.add(1);
            pre = curr;
        }

        return pre;
    }
}