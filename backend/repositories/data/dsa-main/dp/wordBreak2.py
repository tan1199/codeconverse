class TrieNode:
    def __init__(self):
        self.childern = {}
        self.isWord = False
    
    def add(self, word):
        node = self

        for ch in word:
            if(ch not in node.childern): node.childern[ch] = TrieNode()
            node = node.childern[ch]

        node.isWord = True
    
    def __str__(self):
        s =  ""
        for key in self.childern: s += f" {key} : [{str(self.childern[key])}] "
        return s


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        root = TrieNode()
        for word in wordDict: root.add(word)

        @cache
        def helper(index, node):
            if(index == len(s)): 
                return [""] if node.isWord else []
            
            ch = s[index]
            if(ch not in node.childern): return []
            node = node.childern[ch]

            ans = []
            if(node.isWord): for sub_str in helper(index+1, root): ans.append(ch + " " + sub_str)
            for sub_str in helper(index+1, node): ans.append(ch + sub_str)
            return ans

        return helper(0, root)
