from Utils import *

def insertAtIndexK(head: Node, k: int, value: int) -> Node:
    node = head
    new_node = Node(value)
    i  = 0
    while i < k-1 and node is not None:
        node = node.next
        i += 1
    if node is None:
        print("Index out of bounds")
        return head
    new_node.next = node.next
    node.next = new_node
    return head

if __name__ == "__main__":
    linkedList = LinkedList()
    linkedList.add_list([1, 2, 3, 4, 5])
    linkedList.print_list()
    insertAtIndexK(linkedList.head, 2, 10)
    linkedList.print_list()
    insertAtIndexK(linkedList.head, 5, 6)
    linkedList.print_list()