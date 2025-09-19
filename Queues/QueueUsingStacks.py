class Stack:
    def __init__(self):
        self.stack = []
    def isEmpty(self):
        return self.stack == []
    def push(self, data):
        self.stack.append(data)
    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        return None 
    def peek(self):
        if self.isEmpty():
            return None
        return self.stack[-1]

    def size(self):
        return len(self.stack)

class QueueUsingStacks:
    def __init__(self):
        self.S1 = Stack()
        self.S2 = Stack()
		
    def enque(self, data):
        self.S1.push(data)
          
    def move(self):
        if self.S2.isEmpty():
            while not self.S1.isEmpty():
                self.S2.push(self.S1.pop())
        
    def deque(self):
        if self.S2.isEmpty():
            self.move()
        
        return self.S2.pop()
        
    def front(self):
        if self.S2.isEmpty():
            self.move()
        return self.S2.peek()
		


if __name__ == "__main__":
    Q = QueueUsingStacks()
    Q.enque(1)
    Q.enque(2)
    Q.enque(3)
    Q.enque(4)
    Q.enque(5)
    print(f"Deque {Q.deque()}")
    print(f"Front {Q.front()}")
    Q.enque(6)
    print(f"Deque {Q.deque()}")
    print(f"Deque {Q.deque()}")
    print(f"Deque {Q.deque()}")
    Q.enque(7)
    Q.enque(8)
    Q.enque(9)
    Q.enque(10)
    print(f"Deque {Q.deque()}")
    print(f"Deque {Q.deque()}")
    print(f"Deque {Q.deque()}")
    print(f"Deque {Q.deque()}")
    print(f"Deque {Q.deque()}")  # This should return None or raise an error since the queue is empty
    print(f"Front {Q.front()}")  # This should return None or raise an error since the queue is empty   