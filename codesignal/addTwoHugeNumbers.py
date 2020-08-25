"""
You're given 2 huge integers represented by linked lists. Each linked list element is a number from 0 to 9999 that represents a number with exactly 4 digits. The represented number might have leading zeros. Your task is to add up these huge integers and return the result in the same format.
"""


# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#

def reverseLinkedList(l):
    current = l
    previous = None
    head_current = None
    while current != None:
        temp = current.next
        current.next = previous
        previous = current
        if temp == None:
            head_current = current
            current = temp
        else:
            current = temp
    return head_current

def addTwoHugeNumbers(a, b):    
    # Reverse both lists
    head_current_a = reverseLinkedList(a)
    head_current_b = reverseLinkedList(b)
    
    # Add numbers and then add carryover
    head_output_dummy = ListNode(0)
    output_dummy = head_output_dummy
    carry_over = 0
    
    while head_current_a != None and head_current_b != None:
        total = head_current_a.value + head_current_b.value
        total += carry_over
        
        if total > 9999:
            temp = total - 10000
            carry_over = 1
            output_dummy.next = ListNode(temp)
        else:
            carry_over = 0
            output_dummy.next = ListNode(total)
            
        head_current_a = head_current_a.next
        head_current_b = head_current_b.next
        output_dummy = output_dummy.next
    
    # Continue adding rest of linked list
    current_head = None
    if head_current_a != None:
        current_head = head_current_a
    elif head_current_b != None:
        current_head = head_current_b
    while current_head != None:
        total = current_head.value + carry_over
        if total > 9999:
            temp = total - 10000
            carry_over = 1
            output_dummy.next = ListNode(temp)
        else:
            carry_over = 0
            output_dummy.next = ListNode(total)
        
        current_head = current_head.next
        output_dummy = output_dummy.next
    
    # Add new node if there is still a carry over value at the end
    if carry_over > 0:
        output_dummy.next = ListNode(carry_over)
            
    # Reverse Dummy Output and return it
    return reverseLinkedList(head_output_dummy.next)
