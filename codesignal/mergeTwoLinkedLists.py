"""
Note: Your solution should have O(l1.length + l2.length) time complexity, since this is what you will be asked to accomplish in an interview.

Given two singly linked lists sorted in non-decreasing order, your task is to merge them. In other words, return a singly linked list, also sorted in non-decreasing order, that contains the elements from both original lists.
"""

# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def mergeTwoLinkedLists(l1, l2):
    head = new_linked_list = ListNode(0)
    while l1 != None and l2 != None:
        if l1.value == l2.value:
            new_linked_list.next = ListNode(l1.value)
            new_linked_list.next.next = ListNode(l1.value)
            l1 = l1.next
            l2 = l2.next
            new_linked_list = new_linked_list.next.next
        elif l1.value < l2.value:
            new_linked_list.next = ListNode(l1.value)
            l1 = l1.next
            new_linked_list = new_linked_list.next
        else:
            new_linked_list.next = ListNode(l2.value)
            l2 = l2.next
            new_linked_list = new_linked_list.next
    
    if l1 == None or l2 == None:
        rest = l1 if l1 != None else l2
        while rest != None:
            new_linked_list.next = ListNode(rest.value)
            rest = rest.next
            new_linked_list = new_linked_list.next
            
    return head.next
