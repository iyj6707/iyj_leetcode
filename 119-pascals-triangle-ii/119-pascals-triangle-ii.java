class Solution {
    public List<Integer> getRow(int rowIndex) {
        List<Integer> pre = new ArrayList<>();
        
        if(rowIndex == 0){
            return List.of(1);
        }
        
        for(int i=0; i<=rowIndex; i++){
            List<Integer> curr = new ArrayList<>();
            
            if(i == 0){
                curr.add(1);
                pre.add(1);
            }
            else{
                curr.add(1);
                for(int j=1; j<i; j++){
                    curr.add(pre.get(j-1)+pre.get(j));
                }
                curr.add(1);
                pre = curr;
            }
            if(i == rowIndex){
                return pre;
            }
        }

        return null;
    }
}