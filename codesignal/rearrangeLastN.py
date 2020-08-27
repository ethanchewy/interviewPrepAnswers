"""
Note: Try to solve this task in O(list size) time using O(1) additional space, since this is what you'll be asked during an interview.

Given a singly linked list of integers l and a non-negative integer n, move the last n list nodes to the beginning of the linked list.
"""

# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def rearrangeLastN(l, n):
    # 3 pass system
    
    # Edge case 1
    if n == 0:
        return l
        
    original = l
    
    length = 0
    temp = l
    while temp != None:
        temp = temp.next
        length += 1
    
    # Edge case 2
    if n == length:
        return l
    
    start_move_index = length - n
    counter = 0
    second_part = l
    previous = None
    while counter < start_move_index:
        previous= second_part
        second_part = second_part.next
        counter += 1
    
    # Seperate first part from second part
    if previous:
        previous.next = None
    
    head = second_part
    
    # Get to end of second_part and attach it to the head of the first part
    if second_part:
        while second_part.next != None:
            second_part = second_part.next
        second_part.next = original
    
    return head
