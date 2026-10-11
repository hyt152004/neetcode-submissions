class TrieNode:
    def __init__(self):
        # this hashmap will hold the current letter and its children
        self.children = {}
        self.lastLetter = False

class PrefixTree:

    def __init__(self):
        # make a TrieNode class to store children and lastLetter
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # for every letter in word starting from index 0, 
            # check if that letter exists in tree
                # if exists, visit that node and move to next letter
                # else, add that letter node, visit, and move to next letter
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]

        cur.lastLetter = True

    def search(self, word: str) -> bool:
        # start from the root node 
        # for every letter in word
            # for every children node, 
                # check if the node value == current letter 

                # how can i check for the last letter?

        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]

        return cur.lastLetter
        

    def startsWith(self, prefix: str) -> bool:
        # start from the root node 
        # for every letter in word
            # for every children node, 
                # check if the node value == current letter 
                    # 1, continue
                    # 2, return false
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]

        return True

         
        
        