class Solution {
    
    private ArrayList<String> ans = new ArrayList<>();
    private String[] mapping = new String[] {"0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};

    
    public List<String> letterCombinations(String digits) {
        if(digits.length()>0) helper(digits, 0, "");
        return ans;
    }
    
    
    public void helper(String digits, int index, String cur){
        
        if(index==digits.length()){
            ans.add(cur);
            return;
        }
        
        for(char ch: mapping[digits.charAt(index) - '0'].toCharArray()){
            helper(digits, index+1, cur+ch);
        }
    }
    
    
    
}
