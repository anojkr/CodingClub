class Node:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    capacity = 0
    currentSize = 0
    HashMap = {}
    head = Node(-1, -1)
    last = Node(-1, -1)
    head.next = last
    last.prev = head

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.HashMap = {}
        self.currentSize = 0
        self.head.next = self.last
        self.last.prev = self.head

    def get(self, key: int) -> int:
        node = self.HashMap.get(key)
        if node != None:
            self.deleteNode(node.key)
            self.addNode(node.key, node.val)
            return node.val
        return -1

    def deleteNode(self, key):
        node = self.HashMap.get(key)
        if node:
            prevNode = node.prev
            nextNode = node.next
            prevNode.next = nextNode
            nextNode.prev = prevNode
            self.HashMap.pop(node.key)
            self.currentSize -= 1

    def addNode(self, key, val):
        node = Node(key, val)
        frontNode = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = frontNode
        frontNode.prev = node
        self.currentSize += 1
        self.HashMap[node.key] = node

    def put(self, key: int, value: int) -> None:
        node = self.HashMap.get(key)
        if node != None:
            self.deleteNode(key)
            self.addNode(key, value)
        else:
            if (self.currentSize == self.capacity):
                self.deleteNode(self.last.prev.key)
            self.addNode(key, value)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
