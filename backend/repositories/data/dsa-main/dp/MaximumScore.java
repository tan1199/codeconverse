class Solution {
    public int maximumScore(int[] nums, int[] multipliers) {
     
        int[] cur = new int[nums.length];
        int[] prev = new int[nums.length];

        for(int row = multipliers.length-1; row>=0; row--){
            for(int i=row; i<nums.length; i++){
                int mIndex = row - (i) + nums.length -1;
//                System.out.println(row + " " + i + " " + nums.length + " " + mIndex);

                if(0>mIndex || mIndex>=multipliers.length) continue;

                int left = (0<=(i-1) && (i-1)<nums.length) ? cur[i-1] : 0;
                int down = (0<=(i) && (i)<nums.length) ? prev[i] : 0;

//                int left = (0<=row && row<nums.length && 0<=(i-1) && (i-1)<nums.length) ? dp[row][i-1] : 0;
//                int down = (0<=row+1 && row+1<nums.length && 0<=(i) && (i)<nums.length) ? dp[row+1][i] : 0;


//                dp[row][i] = Math.max(
//                        nums[row] * multipliers[mIndex] + down,
//                        nums[i] * multipliers[mIndex] + left
//                );

                cur[i] = Math.max(
                        nums[row] * multipliers[mIndex] + down,
                        nums[i] * multipliers[mIndex] + left
                );
//                System.out.println(cur[i]);
            }
            prev = cur;
        }


//        for(int diff=diffBtwIndex; diff<nums.length; diff++ ){
//            for(int i=0; i+diff<nums.length; i++){
//
//
//                int mIndex = i - (i + diff) + nums.length -1;
//                System.out.println( i + " " + (i+diff) + " " + diff + " " + nums.length + " " + mIndex);
//                System.out.println(dp[i][i+diff]);
//
//                int left = (0<=i && i<nums.length && 0<=(i+diff-1) && (i+diff-1)<nums.length) ? dp[i][i+diff-1] : 0;
//                int down = (0<=i+1 && i+1<nums.length && 0<=(i+diff) && (i+diff)<nums.length) ? dp[i+1][i+diff] : 0;
//
//
//                dp[i][i+diff] = Math.max(
//                        nums[i]*multipliers[mIndex] + down,
//                        nums[i+diff]*multipliers[mIndex] + left
//                );
//            }
//        }

//        for(int[] x:dp) System.out.println(Arrays.toString(x));

//        System.out.println(Arrays.toString(cur) + " " + Arrays.toString(prev));

        return prev[nums.length-1];
    }
}
