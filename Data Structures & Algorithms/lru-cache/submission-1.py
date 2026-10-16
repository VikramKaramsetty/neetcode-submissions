class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} #key:node
        self.left, self.right = Node(-1,0), Node(-1,0)

        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, key):
        node = self.cache[key]
        self.cache.pop(key)
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert(self, key, val):
        if(key in self.cache): self.remove(key)
        node = Node(key,val)
        self.cache[key] = node
        
        self.right.prev.next = node
        node.prev = self.right.prev

        node.next = self.right
        self.right.prev = node

    def get(self, key: int) -> int:
        if(key in self.cache):
            val = self.cache[key].val
            self.insert(key, val)
            return val
        else: return -1

    def put(self, key: int, value: int) -> None:
        if(key not in self.cache and len(self.cache) == self.capacity):
            self.remove(self.left.next.key)
        self.insert(key,value)
        
