class LRUCache:
    class node:
        def __init__(self, key, val):
            self.key = key
            self.val = val
            self.prev = None
            self.next = None

    def __init__(self, capacity: int):
        self.hmap={}
        self.capacity = capacity
        self.head= self.node(-1,-1)
        self.tail= self.node(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head 

    def add(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def remove(self,node):
        node.next.prev = node.prev
        node.prev.next = node.next

    def get(self, key: int) -> int:
        if key not in self.hmap:
            return -1
        node = self.hmap[key]
        self.remove(node)
        self.add(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.hmap:
            old_node = self.hmap[key]
            self.remove(old_node)
            del self.hmap[key]
        node = self.node( key, value)
        self.add(node)
        self.hmap[key]=node

        if len(self.hmap) > self.capacity:
            node_to_del= self.tail.prev
            self.remove(node_to_del)
            del self.hmap[node_to_del.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)