class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
class WordDictionary:

    def __init__(self):
        self.head = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.head
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char] 
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        curr = self.head
        def dfs(word, curr):
            if(word == ""): return curr.endOfWord
            if word[0] in curr.children:
                curr = curr.children[word[0]]
                return dfs(word[1:], curr)
            if word[0] == '.':
                for child in curr.children.values():
                    if dfs(word[1:], child):
                        return True
                return False
        if dfs(word, curr) == True: return True
        return False