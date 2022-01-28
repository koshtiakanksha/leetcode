class TrieNode:
    def __init__(self):
        self.children = {}   # for each character we map it to trienode
        self.word = False    # call a boolean and set it first to false
        
class WordDictionary:
    def __init__(self):
        """ Initialize your data here"""
        self.root = TrieNode()    # to find a root. empty trieNode
        
    def addWord(self, word: str) -> None:
        curr = self.root    
        for c in word:         # iterate through every charcter in word
            if c not in curr.children:    # could've already been inserted
                curr.children[c]= TrieNode()   # we insert a new TrieNode
            curr = curr.children[c]     # update our curr
        curr.word = True    # designated it as a word
        
    def search(self, word: str) -> bool:
        def dfs(j, root):  # j is index character
            curr = root
            for i in range(j, len(word)): # iterate through every charcter in word
                c = word[i]    
                if c == ".":  # if character at index i is "."
                    for child in curr.children.values():
                        if dfs(i+1, child):   # we call dfs functin for every letter
                            return True
                    return False

                else:         # if it is a regular character
                    if c not in curr.children:  # if it is not 
                        return False       # then we simple return False
                    curr = curr.children[c]   # shift our curr pointer to that node
            return curr.word
        return dfs(0,self.root)
# time complexity = O(M)
# space complexity = O(1)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)