"""
Algo:

Insertion:

    A link exists - Move down the tree following the link to the next child level.
             The algorithm continues with searching for the next key character.

    A link does not exist - Then create a new node and link it with the parent's link matching the current key character. 
        Repeat this step until the last character of the key is encountered, 
        then mark the current node as an end node and the algorithm finishes.

Search:
    Check the current node for a link corresponding to the key character.

    A link exist - Move to the next node in the path following the link, 
            and proceed searching for the next key character.

    A link does not exist - If there are no available key characters and current node is marked as isEnd, return true.
        Possible two cases:
        1.   There are key characters left, but it is impossible to follow the key path in the trie, and the key is missing.
        2.   No key characters left, but current node is not marked as isEnd. 
             Therefore the search key is only a prefix of another key in the trie

Starts With:
        Approach is very similar to the one we used for searching a key in a trie.
        The only difference with the approach for search for a key algorithm is that when reached to an end of the key prefix, always return true. 
        No need to consider the isEnd mark of the current trie node

Complexities:

Insertion:
    T.C. - O(m) - m is the key length.
    In each iteration of the algorithm, examine or create a node in the trie until reaching the end of the key. 
    This takes only m operations.

    S.C. - O(m) - m is the key length.
    In the worst case newly inserted key doesn't share a prefix with the the keys already inserted in the trie.
    Add 'm' new nodes, which takes us O(m) space.

Search:
    T.C. - O(m) - m is the key length.
        Search for the next key character. In the worst case the algorithm performs 'm' operations.
    S.C. - O(1)

Starts With:

    T.C. - O(m) - m is the key length.
    S.C. - O(1)
"""

import collections

class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        
    def insert(self, word):
        """
        Inserts a word into the trie.
        """
        current = self.root
        for letter in word:
            current = current.children[letter]
        current.is_word = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        """
        current = self.root
        for letter in word:
            current = current.children.get(letter)
            
            if current is None:
                return False
        return current.is_word
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        current = self.root
        for letter in prefix:
            current = current.children.get(letter)
            if current is None:
                return False
        return True
        


# Your Trie object will be instantiated and called as such:
obj = Trie()

obj.insert("apple")
print (obj.search("apple"))   # returns true
print (obj.search("app"))    # returns false
print (obj.startsWith("app")) # returns true
obj.insert("app") 
print (obj.search("app"))
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)