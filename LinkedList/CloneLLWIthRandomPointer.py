from Utils import *
class RandomLLNode:
	def __init__(self, data = None):
		self.data = data
		self.next = None
		self.random = None

class RandomLinkedList:
    def __init__(self, head=None):
        self.head = head

    def add(self, data):
        if self.head is None:
            self.head = RandomLLNode(data)
        else:
            node = self.head
            while node.next is not None:
                node = node.next
            node.next  = RandomLLNode(data)
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

    def add_random(self, data, random_data):
        current = self.head
        while current is not None:
            if current.data == data:
                break
            current = current.next
        if current is None:
            print("Data not found")
            return
        random_node = self.find(random_data)
        if random_node is None:
            print("Random data not found")
            return
        current.random = random_node	
    def print_list(self):
        current = self.head
        while current is not None:
            random_data = current.random.data if current.random is not None else None
            print(f"Data: {current.data}, Random: {random_data}", end=" -> ")
            current = current.next
        print("None")

def clone(head):
    h1 = None
    h = head

    while h is not None:
        h1 = RandomLLNode(h.data)
        h1.next = h.next
        h.next = h1
        h = h.next.next
    h = head
    while h is not None and h.next is not None:
        h1 = h.next
        h1.random = h.random.next
        h = h.next.next

    #Break the links
    h = head
    head1 = RandomLLNode(-1)
    h1 = head1    
    while h is not None and h.next is not None:
        h1.next = h.next
        h.next = h.next.next
        h = h.next
        h1 = h1.next
    return head1.next


def print_list(head):
    while head is not None:
        print(head.data, end=" -> ")
        head = head.next
    print("None")
	

if __name__ == "__main__":
    rl = RandomLinkedList()
    rl.add_list([1, 2, 3, 4, 5])
    rl.add_random(1, 3)
    rl.add_random(2, 1)
    rl.add_random(3, 5)
    rl.add_random(4, 3)     
    rl.add_random(5, 2)
    print("Original List")
    rl.print_list()
    h = clone(rl.head)
    print("Cloned List")
    cl = RandomLinkedList(h)
    cl.print_list()
    print("Original List")
    rl.print_list()

	

