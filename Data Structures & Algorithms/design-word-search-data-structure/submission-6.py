class WordDictionary:

    def __init__(self):
        self.children = {}
        self.end_of_word = False
        

    def addWord(self, word: str) -> None:
        node = self
        for c in word:
            if c not in node.children:
                node.children[c] = WordDictionary()
            node = node.children[c]
        node.end_of_word = True

    
    # Problem with the search is that there is only a one letter look ahead and must check an arbitrary number of letters ahead
        

    def search(self, word: str) -> bool:
        node = self
        def dfs(node, i):
            if i == len(word):
                return node.end_of_word

            if word[i] == '.':
                for child in node.children.values():
                    if dfs(child, i + 1):
                        return True
                return False
            else:
                if word[i] not in node.children:
                    return False
                return dfs(node.children[word[i]], i + 1)
        
        return dfs(self,0)