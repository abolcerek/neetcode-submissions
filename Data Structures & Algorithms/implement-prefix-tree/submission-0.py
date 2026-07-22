class TrieNode:
    def __init__(self):
        self.children = {} #creating hashmap to store the children 
        self.end = False #creating marker for the end of the word

class PrefixTree:
    def __init__(self): #constructor that creates the root in the trie
        self.root = TrieNode()


    def insert(self, word: str) -> None:
        curr = self.root #creates temp variable at the root of the trie

        for c in word: #looping through every character of every word
            if c not in curr.children: #if the character does not exist in the trie(hashmap)
                curr.children[c] = TrieNode() #we create a new node within the trie for the character
            curr = curr.children[c] #we set the variable curr to the node of the character
        curr.end = True


    def search(self, word: str) -> bool:
        curr = self.root

        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.end

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True




