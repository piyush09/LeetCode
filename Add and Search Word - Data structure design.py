"""
Algo, T.C., S.C.:

Add Word in Trie:
    In trie, each path from the root to the "word" node represents one of the input words.
    Trie is basically nested hashmaps.
    Verify, if the child node to add is already present. If yes, just go one step down. 
        If not, add it into the trie and then go one step down.

T.C. - O(M) - where M is the key length. 
            At each step, either examine or create a node in the trie. 
            That takes only M operations.

S.C. - O(M) - where M is the key length.
        In the worst-case newly inserted key doesn't share a prefix with the keys already inserted in the trie. 
        So, need to add 'M' new nodes, which takes O(M) space.      

Search in Trie:

    In the absence of '.' characters, the search is as simple as addWord. 
    Each key is represented in the trie as a path from the root to the internal node or leaf. 
    Start from the root and go down in trie, checking character by character.

    The presence of '.' characters forces to explore all possible paths at each '.' level.

T.C. - O(M) for the "well-defined" words without dots, where M is the key length, and N is number of keys.
        O(M*N) - for undefined words, which in the worst case would be searching an undefined word (M+1), 
        which is one character longer than all inserted keys.

S.C. - O(1) for the search of "well-defined" words without dots, 
       and up to O(M) for the "undefined" words, to keep the recursion stack.
"""

import collections
import re

class TrieNode():
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        """
        node = self.root
        for w in word:
            node = node.children[w]
        node.isWord = True
        

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        node = self.root
        self.res = False
        self.dfs(node, word)
        return self.res

    def dfs(self, node, word):
        if not word:
            if node.isWord:
                self.res = True
            return

        if (word[0] == "."):
            for n in node.children.values():
                self.dfs(n, word[1:])

        else:
            node = node.children.get(word[0])
            if not node:
                return
            self.dfs(node, word[1:])

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

obj = WordDictionary()
obj.addWord("bad")
obj.addWord("dad")
obj.addWord("mad")

print(obj.search("pad"))
print(obj.search("bad"))
print(obj.search(".ad"))
print(obj.search("b.."))
