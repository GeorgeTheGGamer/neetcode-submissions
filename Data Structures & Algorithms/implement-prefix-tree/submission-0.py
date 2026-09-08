class PrefixTree:

    # Each node holds the children below it and whether it is the end of word
    def __init__(self):
        # The hashmap holds for node for each letter
        self.children = {} 
        self.end_of_word = False
        

    # Must go through each letter until we find not in children then make a new node then end of word
    def insert(self, word: str) -> None:
        node = self
        for c in word:
            if c not in node.children:
                node.children[c] = PrefixTree()
            node = node.children[c]
        node.end_of_word = True

    
    # Loop through each character until through all, then return the end of word if word is in here
    def search(self, word: str) -> bool:
        node = self
        for c in word:
            if c not in node.children:
                return False
            else:
                node = node.children[c]
        
        return node.end_of_word             # This represents if word is present cause could be set to False
        

    # Only care if letters in it and not specifically the word is in there
    def startsWith(self, prefix: str) -> bool:
        node = self
        for c in prefix:
            if c not in node.children:
                return False
            else:
                node = node.children[c]
        
        return True
        