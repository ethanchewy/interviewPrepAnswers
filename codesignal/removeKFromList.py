"""
Note: Try to solve this task in O(n) time using O(1) additional space, where n is the number of elements in the list, since this is what you'll be asked to do during an interview.

Given a singly linked list of integers l and an integer k, remove all elements from list l that have a value equal to k.
"""


# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def removeKFromList(l, k):
    head = l
    pointer = l
    previous = None
    
    while pointer != None:
        if pointer.value == k:
            if head == pointer:
                head = pointer.next
            else:
                previous.next = pointer.next
        previous = pointer
        pointer = pointer.next
    
    return head
