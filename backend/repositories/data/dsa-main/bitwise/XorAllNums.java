class Solution {
    public int xorAllNums(int[] nums1, int[] nums2) {
        if(nums1.length%2==0 && nums2.length%2==0){
            return 0;
        } 
        
        if(nums1.length%2==1 && nums2.length%2==1){
            int ans = 0;
            for(int x: nums1) ans = ans ^ x;
            for(int x: nums2) ans = ans ^ x;
            return ans;
        }
        
        if(nums1.length%2==0 && nums2.length%2==1){
            int ans = 0;
            for(int x: nums1) ans = ans ^ x;
            return ans;
        }
        
        if(nums1.length%2==1 && nums2.length%2==0){
            int ans = 0;
            for(int x: nums2) ans = ans ^ x;
            return ans;
        }
        
        return 0;
    }
}
