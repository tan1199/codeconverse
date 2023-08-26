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
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        root = TrieNode()
        for word in wordDict: root.add(word)

        @cache
        def helper(index, node):
            if(index == len(s)): 
                return True if node.isWord else False
            
            ch = s[index]
            if(ch not in node.childern): return False
            node = node.childern[ch]
            if((node.isWord and helper(index+1, root)) or helper(index+1, node)): return True

        return helper(0, root)
