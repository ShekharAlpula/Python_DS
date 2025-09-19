from NearestOperations import Stack

def NSL(A):
    nsl = []
    stack = Stack()
    print(f"NSL : Input array {A}")
    for i in range(len(A)):
        while not stack.isEmpty() and A[i] <= A[stack.peek()]:
                stack.pop()
        if stack.isEmpty():
             nsl.append(-1)
        else:
             nsl.append(stack.peek())

        stack.push(i)
    
    return nsl

def NSR(A):
    nsr = []
    stack = Stack()
    print(f"NSR : Input array {A}")
    N = len(A)

    for i in range(len(A)-1, -1, -1):
        while  not stack.isEmpty() and A[i] <= A[stack.peek()]:
            stack.pop()
        
        if stack.isEmpty() :
                nsr.append(N)
        else:
            nsr.append(stack.peek())
        stack.push(i)   

    return nsr[::-1]  # Reverse the result to match the original order

def NGL(A):
    ngl = []
    stack = Stack()
    print(f"NGL : Input array {A}")
    for i in range(len(A)):
        while not stack.isEmpty() and A[i] >= A[stack.peek()]:
            stack.pop()
        
        if stack.isEmpty():
             ngl.append(-1)
        else:
            ngl.append(stack.peek())

        stack.push(i)
    return ngl

def NGR(A):
    ngr = []
    stack = Stack()
    print(f"NGR : Input array {A}")

    for i in range(len(A)-1, -1, -1):
        while  not stack.isEmpty() and A[i] >= A[stack.peek()]:
            stack.pop()
        
        if stack.isEmpty() :
                ngr.append(-1)
        else:
            ngr.append(stack.peek())
        stack.push(i)   

    return ngr[::-1]  # Reverse the result to match the original order

def findMaxRectArea(A):
    nsl = NSL(A)
    nsr = NSR(A)
    ngl = NGL(A)
    ngr = NGR(A)

    max_area = 0
    for i in range(len(A)):
         area = A[i] * ( nsr[i] - nsl[i] -1 )
         max_area = max(max_area, area)
    
    print(f"Maximum rectangular area in histogram is {max_area}")

if __name__ == "__main__":
    A = [8, 6, 2, 5, 6, 5, 7, 4]
    findMaxRectArea(A)

    

