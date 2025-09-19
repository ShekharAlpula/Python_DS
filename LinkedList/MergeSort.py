from Utils import *

def findMiddle(head : Node) -> Node:
    if head is None or head.next is None:
        return head
    
    s = head
    f = head.next
    while f is not None and f.next is not None:
        s = s.next
        f = f.next.next
    return s

def merge(L1 : Node, L2: Node) -> Node:
    head = Node(-1)
    h = head
    l1 = L1
    l2 = L2

    while l1 is not None and l2 is not None:
        if l1.data <= l2.data:
            h.next = l1
            l1 = l1.next
        else:
            h.next = l2
            l2 = l2.next
        
        h = h.next

    ##Remaining elements
    if l1 is not None:
        h.next = l1
    if l2 is not None:
        h.next = l2

    return head.next

def mergeSort(head: Node) -> Node:

    if head is None or head.next is None:
        return head
    
    print(f"head data is {head.data}")
    if head.next is not None:
        print(f"next data is {head.next.data}")

    m = findMiddle(head)
    print(f"Middle data is {m.data}")
    l1 = head
    l2 = m.next;
    m.next = None
    l1 = mergeSort(l1)
    l2 = mergeSort(l2)
    return merge(l1, l2)


if __name__ == "__main__":
    linkedList = LinkedList()
    linkedList.add_list([15, 3, 24, 6, 12, 18, 22, 28, 32, 44, 56])
    linkedList.print_list()
    """m = findMiddle(linkedList.head)
    print("Middle element is", m.data)"""
    head = mergeSort(linkedList.head)
    linkedList.head = head
    print("Sorted List")
    linkedList.print_list()



    
