"""
Note: Try to solve this task in O(n) time using O(1) additional space, where n is the number of elements in l, since this is what you'll be asked to do during an interview.

Given a singly linked list of integers, determine whether or not it's a palindrome.

Note: in examples below and tests preview linked lists are presented as arrays just for simplicity of visualization: in real data you will be given a head node l of the linked list
"""


# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def isListPalindrome(l):
    # Find length of linked list
    count = 0
    temp = l
    while temp != None:
        count += 1
        temp = temp.next
    
    # Find pointer to second half
    temp2 = l
    counter = 0
    mid_point_index = count // 2
    if count % 2 != 0:
        mid_point_index = count // 2 + 1
    mid_point = None
    while mid_point == None:
        if counter == mid_point_index:
            mid_point = temp2
            break
        temp2 = temp2.next
        counter += 1
    
    # Reverse second half iteratively in constant space
    previous = None
    current = mid_point
    head_reversed_list = None
    while current != None:
        temp = current.next
        current.next = previous
        previous = current
        if temp == None:
            head_reversed_list = current
            current = temp
        else:
            current = temp
            
    # Compare
    while head_reversed_list != None and l != None:
        if head_reversed_list.value != l.value:
            return False
        head_reversed_list = head_reversed_list.next
        l = l.next
    
    return True
