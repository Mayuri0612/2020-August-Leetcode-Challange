class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashTable = [[] for _ in range(10000)]
    
    
    def hashfunc(self,key):
        return key % len(self.hashTable)
        
        

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        hash_key = self.hashfunc(key)
        if not self.contains(key):
            self.hashTable[hash_key].append(key)
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        hash_key = self.hashfunc(key)
        if self.contains(key):
            self.hashTable[hash_key].remove(key)
        

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        hash_key = self.hashfunc(key)
        return key in self.hashTable[hash_key]