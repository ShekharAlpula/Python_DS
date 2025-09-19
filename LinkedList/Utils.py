class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class DLLNode:
    def __init__(self, data=None):
        self.data = data;
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self, head=None):
        self.head = head

    def add(self, data):
        if self.head is None:
            self.head = DLLNode(data)
        else:
            node = self.head
            while node.next is not None:
                node = node.next
            nn = DLLNode(data)
            nn.prev = node
            node.next = nn
        return self.head
    
    def add_list(self, lst):
        for i in lst:
            self.add(i)

    def print_list(self):
        node = self.head
        while node is not None:
            print(node.data, end="->")
            node = node.next
        print("None")

    def remove(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            head = self.head.next
            head.prev = None
            return
        
        node = self.head
        while node is not None:
            if node.data == data:
                print("Removing", node.data)
                node.prev.next = node.next
                if node.next is not None:
                    node.next.prev = node.prev
                return
            node = node.next



class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def add(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            node = self.head
            while node.next is not None:
                node = node.next
            node.next  = Node(data)
        return self.head    

    def add_list(self, lst):
        for i in lst:
            self.add(i)
        return self.head
    
    def find(self,data):
        current = self.head
        while current is not None:
            if current.data == data:
                return current
            current = current.next
        return None
    

    def remove(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next is not None:
            if current.next.data == data:
                print("Removing", current.next.data)
                current.next = current.next.next
                return
            current = current.next


    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

def LinkedListDriver():
    linkedList = LinkedList()
    linkedList.add_list([1, 2, 3, 4, 5])
    linkedList.print_list()
    linkedList.remove(3)
    linkedList.print_list()

def DoubleLinkedListDriver():
    print("Double Linked List")
    dll = DoubleLinkedList()
    dll.add_list([1, 2, 3, 4, 5])
    dll.print_list()
    dll.remove(3)
    dll.print_list()


if __name__ == "__main__":
    #LinkedListDriver()
    DoubleLinkedListDriver()



 