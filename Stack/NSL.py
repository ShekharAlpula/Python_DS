class Stack:
    from collections import deque
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return len(self.stack) == 0
    
    def peek(self):
        return self.stack[-1]
    
    def push(self, val):
       self.stack.append(val)

    def pop(self):
      self.stack.pop()

    def __str__(self):
        string = ""
        for i in range(0, len(self.stack) ):            
            string = string + str(self.stack[i])
            string = string + " "
        return string
            #print(self.stack[i], end="  ")


def NSL():
    ##stack
    stack = Stack()
    nsl = []
    A = [1, 3, 10, 2, 8, 7, 6, 7, 1]
    print(f"Input array {A}")

    for i in range(0, len(A)):
        
        while stack.isEmpty() == False and A[i] <= A[stack.peek()]:
            stack.pop()

        if stack.isEmpty() == True:
            nsl.append(-1)
        else :
            nsl.append(A[stack.peek()])
        stack.push(i)

    print(f"NSL : {nsl}")

if __name__ == "__main__":
    NSL()