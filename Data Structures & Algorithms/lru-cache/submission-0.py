class Node:
    def __init__(self, key,  val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
        

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.right = Node(0,0)
        self.left = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    # remove node from list
    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    # insert node at right
    def insert(self, node):
        prev = self.right.prev
        nxt = self.right
        prev.next = node
        nxt.prev = node
        node.next = nxt
        node.prev = prev




    def put(self, key: int, value: int) -> None:
        if key in self.cache:  #same node exists, so remove
            self.remove(self.cache[key])
        
        self.cache[key] = Node(key,value)  # add to map
        self.insert(self.cache[key])   # add to linked list

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

