class Solution {
    public int numRollsToTarget(int n, int k, int target) {
        int[][] dp = new int[n+1][target+1];
        
        for(int i=1; i<=k && i<=target; i++){
            dp[1][i] = 1;
        }
        
        for(int i=2; i<=n; i++){
            for(int j=0; j<=target; j++){
                dp[i][j] = (int) getVal(dp,i,j,k);
            }
        }
        
        return dp[n][target]; 
    }
    
    
    public long getVal(int[][] dp, int row, int col, int k){
        int mod = 1000000007;
        int val = 0;
        for(int index = col-1; index>=0 && k>0; index--){
            val = (val + dp[row-1][index])%mod;
            k-=1;
        }
        return val;
    }
    
}
