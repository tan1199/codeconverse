class Solution {
    public int[] smallestSubarrays(int[] nums) {
        
        int[] backward = new int[nums.length];
        int index = nums.length - 1;
        backward[index] = nums[index];
        index--;
        
        while(index>=0){
            backward[index] = backward[index+1] | nums[index];
            index--;
        }
                
        index = 0;
        int index2 = 0;
        int or = 0;
        
        int[] bitCount = new int[32];
        int[] ans = new int[nums.length];
        
        
        while(index2<nums.length && or!=backward[index]) {
            for(int i=0;i<=30;i++){
                if(((1<<i) & nums[index2]) != 0) bitCount[i]++;
            }
            or = or | nums[index2];
            index2++;
        }
        
        if(index2<index){
            index2 = index;
        }
        
        
        
        
        ans[index] = index2 - index;
        if(ans[index]==0) ans[index] = 1;
        index++;
        
        while(index<nums.length){
            
            if(index2<index){
                index2 = index;
            }
            
            int prev = index-1;
            
            for(int i=0;i<=30;i++){
                if(((1<<i) & nums[prev]) != 0) {
                    if(bitCount[i]==1){
                        or = or^(1<<i);
                    }
                    bitCount[i]--;
                }
            }            
            
            while(index2<nums.length && or!=backward[index]) {
                for(int i=0;i<=30;i++){
                    if(((1<<i) & nums[index2]) != 0) bitCount[i]++;
                }
                or = or | nums[index2];
                index2++;
            }
            
            
            ans[index] = index2 - index;
            if(ans[index]==0) ans[index] = 1;
            index++;
        }
                
        return ans;
    }
}
