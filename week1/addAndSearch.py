class Node:
    
    def __init__(self, value = None):
        self.value = value
        self.seq = {}

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node("")

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        tmp = self.root
        for i, letter in enumerate(word):
            if letter not in tmp.seq:
                tmp.seq[letter] = Node()
                
            tmp = tmp.seq[letter]
                
        tmp.value = word

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        tmp = self.root
        for i in range(len(word)):                                
            if word[i] == ".":
                valid = False
                for nxt in tmp.seq.keys():
                    valid = valid or self.search(word[:i] + nxt + word[i+1:])
                    
                    if valid:
                        return True
                return False
            
            if word[i] not in tmp.seq:
                return False 
            tmp = tmp.seq[word[i]]
                
        return tmp.value == word