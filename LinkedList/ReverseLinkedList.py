from Utils import *

def reverse(head):
    nh = None
    while head is not None:
        next = head.next
        head.next = nh
        nh = head
        head = next
    return nh

if __name__ == "__main__":
    ll = LinkedList()
    ll.add_list([1, 2, 3, 4, 5])
    ll.print_list()
    head = reverse(ll.head)

    ll.head = head
    ll.print_list()

