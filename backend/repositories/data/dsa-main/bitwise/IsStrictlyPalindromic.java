class Solution {
    public boolean isStrictlyPalindromic(int n) {
        for(int i=2;i<=(n-2);i++){
            // System.out.println(getBaseString(n,i));
            if(!isPalindrome(getBaseString(n,i))) return false;
        }
        
        return true;
    }
    
    public boolean isPalindrome(String s){
        int i=0;
        int j=s.length()-1;
        while(i<j){
            if(s.charAt(i)!=s.charAt(j)) return false;
            i++;
            j--;
        }
        return true;
    }
    
    public String getBaseString(int n, int base){
        StringBuffer ans = new StringBuffer();
        while(n>0){
            ans.append((n%base)+"");
            n = n/base;
        }
        
        return ans.reverse().toString();
    }
}
