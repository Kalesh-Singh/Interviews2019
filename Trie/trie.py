from collections import defaultdict

class Node(object):
    def __init__(self):
        self.children = defaultdict(Node)
        self.end = False

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr_node = self.root
        for char in word:
            curr_node =  curr_node.children[char]
        curr_node.end = True


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curr_node = self.root
        for char in word:
            if char not in curr_node.children:
                return False
            curr_node = curr_node.children[char]
        return curr_node.end
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curr_node = self.root
        for char in prefix:
            if char not in curr_node.children:
                return False
            curr_node = curr_node.children[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
