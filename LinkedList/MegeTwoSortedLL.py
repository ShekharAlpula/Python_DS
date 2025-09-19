from Utils import *

def mergeLists(L1 : Node, L2: Node) -> Node:
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
    if l1 is None:
        h.next = l2
    else:
        h.next = l1        
    return head.next


if __name__ == "__main__":
    eL = LinkedList()
    eL.add_list([2,4,6,12,18, 22, 28, 32, 44,56])
    eL.print_list()

    oL = LinkedList()
    oL.add_list([1,5,11,15,51])
    oL.print_list()
    merged = mergeLists(eL.head, oL.head)
    mL = LinkedList(merged)
    print("Merged List")
    mL.print_list()
