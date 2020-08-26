"""
Note: Your solution should have O(n) time complexity, where n is the number of elements in l, and O(1) additional space complexity, since this is what you would be asked to accomplish in an interview.

Given a linked list l, reverse its nodes k at a time and return the modified list. k is a positive integer that is less than or equal to the length of l. If the number of nodes in the linked list is not a multiple of k, then the nodes that are left out at the end should remain as-is.

You may not alter the values in the nodes - only the nodes themselves can be changed.

Example

For l = [1, 2, 3, 4, 5] and k = 2, the output should be
reverseNodesInKGroups(l, k) = [2, 1, 4, 3, 5];
For l = [1, 2, 3, 4, 5] and k = 1, the output should be
reverseNodesInKGroups(l, k) = [1, 2, 3, 4, 5];
For l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] and k = 3, the output should be
reverseNodesInKGroups(l, k) = [3, 2, 1, 6, 5, 4, 9, 8, 7, 10, 11].

"""


# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#

def reverseLinkedPart(l, count):
    current = l
    previous = None
    i = 0
    while current != None and i < count:
        temp = current.next
        current.next = previous
        previous = current
        current = temp
        i += 1
    return previous

def reverseNodesInKGroups(l, k):
    index = 0
    
    starting = None
    
    head = l
    previous = None
    
    # last part of the current reversed kth part linked list
    end_part = head
    
    # last element of the kth part reversed before
    end_part_previous = None
    
    while head != None:
        
        # Keep track of the next element just in case it gets changed in reversing process
        temp_next = head.next
        
        # Reverse each part if we are the kth value
        if (index + 1) % k == 0:
            
            # temp equals the "head" element of the reversed linked part
            temp = reverseLinkedPart(end_part, k)
            
            # Connect previous kth part with the head of the current one
            if end_part_previous != None:
                end_part_previous.next = temp
            
            # Keep track of the previous reversed list before
            end_part_previous = end_part
            
            # Start tracking the last element of the next reversed list
            end_part = temp_next
            
            
            # Record the "first" starting point of the whole reversed linked list
            if index + 1 == k:
                starting = temp

        head = temp_next
        index += 1
    
    # Append non reversed elements at the end
    if (index - 1 + 1) % k != 0:
        while end_part != None:
            end_part_previous.next = end_part
            end_part_previous = end_part_previous.next
            end_part = end_part.next
        end_part_previous.next = None

    return starting
    
