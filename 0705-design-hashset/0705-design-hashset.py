class MyHashSet:
    def __init__(self):
        self.primaryBuckets = 1000
        self.secondaryBuckets = 1000
        self.storage = [None] * self.primaryBuckets

    def getPrimaryHash(self, key):
        return key % self.primaryBuckets

    def getSecondaryHash(self, key):
        return key // self.secondaryBuckets

    def add(self, key):
        primaryIndex = self.getPrimaryHash(key)
        if self.storage[primaryIndex] is None:
            if primaryIndex == 0:
                self.storage[primaryIndex] = [False] * (self.secondaryBuckets + 1)
            else:
                self.storage[primaryIndex] = [False] * self.secondaryBuckets
        secondaryIndex = self.getSecondaryHash(key)
        self.storage[primaryIndex][secondaryIndex] = True

    def remove(self, key):
        primaryIndex = self.getPrimaryHash(key)
        if self.storage[primaryIndex] is None:
            return
        secondaryIndex = self.getSecondaryHash(key)
        self.storage[primaryIndex][secondaryIndex] = False

    def contains(self, key):
        primaryIndex = self.getPrimaryHash(key)
        if self.storage[primaryIndex] is None:
            return False
        secondaryIndex = self.getSecondaryHash(key)
        return self.storage[primaryIndex][secondaryIndex]
