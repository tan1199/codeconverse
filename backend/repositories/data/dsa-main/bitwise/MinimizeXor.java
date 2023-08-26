class Solution {
    public int minimizeXor(int num1, int num2) {
        int n2 = getnumBits(num2);
        int n1 = getnumBits(num1);
        
        // System.out.println(n1 + " " + n2);
        
        if(n2 == n1) return num1;
        int ans = 0;
        
        while(n2>0 && n1>0){
            int len = (int) (Math.log(num1) / Math.log(2) + 1);
            num1 = num1 ^ (1<<len-1);
            ans = ans | (1<<len-1);
            n1--;
            n2--;
        }
        
        // System.out.println(ans);
        
            for(int i=0;i<=31 && n2>0;i++){
                int val = 1<<i;
                // System.out.println(i + " " +  val);
                if((val&ans)==0){
                    ans = ans ^ val;
                    n2--;
                }
            }
        
        return ans;
    }
    
    public int getnumBits(int num2){
        int n = 0;
        while(num2>0){
            num2 = num2 & (num2-1);
            n++;
        }
        return n;
    }
}
