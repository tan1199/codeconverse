class Solution {
    public int numberOfWays(int startPos, int endPos, int k) {
        if(endPos<startPos) return numberOfWays(endPos, startPos, k);

        if(startPos+k < endPos) return 0;
        
        int xysum = k;
        int xysub = endPos - startPos;
        
        if((xysum + xysub)%2 == 1) return 0;
        
        int x = (xysum + xysub)/2;
        int y = xysum - x;
        
        return ncr(k, x);
    }
    
    public int ncr(int n, int r){
        int[][] ans = new int[n+1][n+1];
        ans[0][0] = 1;

        for(int i = 1; i <= n; i++) {
            ans[i][0] = 1;
            for(int j = 1; j <= i; j++) {
                ans[i][j] = (ans[i - 1][j - 1] + ans[i - 1][j]) % (1000000007);
            }
        }
        return ans[n][r];
    }
    
}
