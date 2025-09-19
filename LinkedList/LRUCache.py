from collections import deque
class ListNode:
    def __init__(self, value : int):
        self.value = value
        self.next = None
        self.prev = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, value: int):
        node = ListNode(value)
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        return node

    def dequeue(self) -> int:
        if self.head is None:
            return -1
        value = self.head.value
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
        else:
            self.tail = None
        self.size -= 1
        return value    

    def remove(self, node : ListNode) -> None:
        if node is None:
            return
        if node.prev is not None:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next is not None:
            node.next.prev = node.prev
        else:
            self.tail = node.prev
        self.size -= 1

        
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.queue = Queue()
    
        
    def remove(self, key: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            del self.cache[key]
            # Remove the node from the queue
            if node is self.queue.head:
                node.next.prev = node.prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.queue.remove(key)
            # Move the accessed item to the end of the queue
            new_node = self.queue.enqueue(key)
            self.cache[key] = new_node
            return key
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.queue.remove(node)
            # Update the value and move it to the end of the queue
            new_node = self.queue.enqueue(key)
            self.cache[key] = new_node            
        else:
            if len(self.cache) >= self.capacity:
                # Evict the least recently used item
                lru_key = self.queue.dequeue()
                if lru_key != -1:
                    del self.cache[lru_key]
            # Add the new key-value pair            
            node = self.queue.enqueue(key)
            self.cache[key] = node

if __name__ == "__main__":
    lru = LRUCache(3)
    lru.put(1, 1)  # cache is {1=1}
    lru.put(2, 2)  # cache is {1=1, 2=2}
    print(lru.get(1))  # returns 1
    lru.put(3, 3)      # cache is {1=1, 2=2, 3=3}
    print(lru.get(2))  # returns 2
    lru.put(4, 4)      # evicts key 1, cache is {2=2, 3=3, 4=4}
    print(lru.get(1))  # returns -1 (not found)
    print(lru.get(3))  # returns 3
    print(lru.get(4))  # returns 4