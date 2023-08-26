package com.akarsh.designpatterns;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class WordSearch2 {
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.findWords(
                new char[][]{
                        {'o','a','a','n'},
                        {'e','t','a','e'},
                        {'i','h','k','r'},
                        {'i','f','l','v'}
                },
                new String[]{"oath","pea","eat","rain"}
        ));
    }
}


class Solution {
    public List<String> findWords(char[][] board, String[] words) {
        TrieNode root = new TrieNode();
        List<String> ans = new ArrayList<>();


        for (String word: words) {
            TrieNode node = root;
            for (Character ch: word.toCharArray()){
                if(!node.hasChild(ch)) {
                    node.setChild(ch, new TrieNode());
                }
                node = node.getChild(ch);
            }
            node.setWord(word);
        }

        boolean[][] visited = new boolean[board.length][board[0].length];

        for (int i=0;i<board.length;i++){
            for (int j=0; j<board[0].length; j++){
                helper(i ,j, board, root, ans, visited);
            }
        }

        return ans;
    }

    public void helper(int i, int j, char[][] board, TrieNode node, List<String> ans, boolean[][] visited){

        if(i<0 || j<0 || i>=board.length || j>=board[0].length || visited[i][j]) return;
        if(!node.hasChild(board[i][j])) return;

        Character ch = board[i][j];
        node = node.getChild(ch);

        if(node.getWord() != null ) {
            ans.add(node.getWord());
        }

        visited[i][j] = true;

        helper(i-1, j, board, node, ans, visited);
        helper(i, j+1, board, node, ans, visited);
        helper(i+1, j, board, node, ans, visited);
        helper(i, j-1, board, node, ans, visited);

        visited[i][j] = false;
    }

}

class TrieNode{
    private String word;
    private final TrieNode[] children;

    public TrieNode(){
        word = null;
        children = new TrieNode[26];
    }

    public void setWord(String word) {
        this.word = word;
    }

    public String getWord() {
        return word;
    }

    public boolean hasChild(Character ch){
        return children[ch - 'a'] != null;
    }

    public TrieNode getChild(Character ch) {
        return children[ch-'a'];
    }

    public void setChild(Character ch, TrieNode child) {
        this.children[ch-'a'] = child;
    }

    @Override
    public String toString() {
        return "TrieNode{" +
                "Word=" + word +
                ", children=" + Arrays.toString(children) +
                '}';
    }
}
