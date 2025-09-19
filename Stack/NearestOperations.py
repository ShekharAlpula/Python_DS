class Stack:
    def __init__(self):
        self.stack= []

    def isEmpty(self):
            return len(self.stack) == 0
    
    def peek(self):
        if not self.isEmpty():
            return self.stack[-1]
        return None
    
    def push(self, val):
        self.stack.append(val)

    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        return None
    def __str__(self):
        return " ".join(str(x) for x in self.stack)
    
def NSL(A):
    nsl = []
    stack = Stack()
    print(f"Input array {A}")
    for i in range(len(A)):
        while stack.isEmpty() == False and A[i] <= A[stack.peek()]:            
            stack.pop()
        if stack.isEmpty():
            nsl.append(-1)
        else:
            nsl.append(A[stack.peek()])

        stack.push(i)
    return nsl


def NSR(A):
    nsr = []
    stack = Stack()
    print(f"Input array {A}")
    for i in range(len(A)-1, -1, -1):
        print(f"Processing element {A[i]} at index {i}")
        print(f"Current stack: {stack}")
        while stack.isEmpty() == False and A[i] <= A[stack.peek()]:
            stack.pop()   
        if not stack.isEmpty():
            print(f"Current stack peek : {A[stack.peek()]}")   

        if stack.isEmpty():
            nsr.append(-1)
        else:
            nsr.append(A[stack.peek()])

        stack.push(i)
    return nsr[::-1]  # Reverse the result to match the original order

def NGL(A):
    ngl = []
    statck = Stack()
    print(f"Input array {A}")
    for i in range(len(A)):
        while stack.isEmpty() == False and A[i] >= A[stack.peek()]:
            stack.pop()
        if stack.isEmpty():
            ngl.append(-1)
        else:
            ngl.append(A[stack.peek()])
        stack.push(i)

    return ngl

def NGR(A):
    ngr = []
    stack = Stack()
    print(f"Input array {A}")
    for i in range(len(A)-1, -1, -1):
        while stack.isEmpty() == False and A[i] >= A[stack.peek()]:
            stack.pop()
        
        if stack.isEmpty():
            ngr.append(-1)
        else:
            ngr.append(A[stack.peek()])
        stack.push(i)
    return ngr[::-1]  # Reverse the result to match the original order

if __name__ == "__main__":
    stack = Stack()
    A = [1, 3, 10, 2, 8, 7, 6, 7, 1]
    nsl = NSL(A)

    print(f"NSL : {nsl}")
    nsr = NSR(A)
    print(f"NSR : {nsr}")    

    ngl = NGL(A)
    print(f"NGL : {ngl}")

    ngr = NGR(A)
    print(f"NGR: {ngr}")
