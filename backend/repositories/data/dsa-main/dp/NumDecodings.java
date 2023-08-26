class Solution {
    public int numDecodings(String s) {

        final int n = s.length();
        int[] ans = new int[n];
        
        ans[n-1] = s.charAt(n-1) != '0' ? 1 : 0;
        
        if(n>=2){
            ans[n-2] = isValid(s.substring(n-2)) * 1 +  isValid(s.substring(n-2,n-1)) * ans[s.length()-1];
        }
        
        for(int index = n-3; index>=0; index--){
            ans[index] = isValid(s.substring(index,index+2)) * ans[index+2] +  isValid(s.substring(index,index+1)) * ans[index+1];
        }
        
        // System.out.println(Arrays.toString(ans));
        
        return ans[0];
    }
    
    
    public int isValid(String s){
        // System.out.println(s);
        if(s.charAt(0)=='0') return 0;
        int val = Integer.parseInt(s);
        return (val>=1 && val<=26) ? 1 :0;
    }
}
