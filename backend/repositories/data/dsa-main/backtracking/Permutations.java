class Solution {
    public List<List<Integer>> permute(int[] nums) {
        boolean[] added = new boolean[nums.length];
        List<List<Integer>> ans = new ArrayList<List<Integer>>();
        permute(nums, added, ans, new ArrayList<Integer>());
        return ans;
    }
    
    public void permute(int[] nums, boolean[] added, List<List<Integer>> ans, ArrayList<Integer> cur){
        
        if(cur.size() == nums.length) {
            ans.add(new ArrayList(cur));
            return;
        }
        
        for(int index=0; index<nums.length; index++){
            
            if(added[index]) continue;
            
            added[index] = true;
            cur.add(nums[index]);
            permute(nums, added, ans, cur);
            added[index] = false;
            cur.remove(cur.size()-1);
        }
    }
    
    
    
}
